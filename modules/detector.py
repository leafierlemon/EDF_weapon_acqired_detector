import difflib
from google.cloud import vision
import csv
from PIL import Image


class Detector:
    def __init__(self,tablePath,trim,credential,filter={},tmpDir="./tmp/"):
        self.tmpDir=tmpDir
        self.trim=trim
        self.m=Matcher(tablePath,filter)
        self.ocr=GCV(credential)
        
    def __del__(self):
        del self.m
        del self.ocr

    def setMatcher(self,tableDir,presuffix):
        del self.m
        self.m=Matcher(tableDir,presuffix)



    def do(self,img,tmpfilename="tmp.png"):
        img_gt=trim(img,self.trim["range"],self.trim["base"])
        tmpPath=self.tmpDir+tmpfilename
        img_gt.save(tmpPath)
        out_raw=self.ocr.image_to_string(tmpPath)
        # print(out_raw)
        out_m=self.m.match_l(out_raw)

        return out_m

def trim(img, box, base=(1920, 1080)):
    WIDTH,HEIGHT=img.size
    img_gray = img.convert("L")

    selected = [WIDTH*box[0]//base[0], HEIGHT*box[1]//base[1],
                WIDTH*box[2]//base[0], HEIGHT*box[3]//base[1]]

    return img_gray.crop(selected)

class Matcher:
    def __init__(self, table,presuffix):
        with open(table, encoding='utf-8')as f:
            r = csv.reader(f)
            self.table = [l for l in r if l[0][:2] != "# " and len(l[0])]
            for r in self.table:
                if len(r) == 1:
                    r.append(r[0])
        self.presuffix=presuffix
        return

    def match(self, str):

        UPNEW=""
        flg=False
        for key, value in self.presuffix.items():
            l=len(key)
            if str[len(str)-l:]==key:
                UPNEW=key
                str=str[:len(str)-l]
                flg=True                
                break
        if not flg:
            return ""

        l_ratio = []
        for w_n, w_m in self.table:
            l_ratio.append(difflib.SequenceMatcher(None, str, w_m).ratio())
        m = max(l_ratio)
        th = 0.5
        text = ""
        if m > th:
            text = self.table[l_ratio.index(m)][0]

        return self.presuffix[UPNEW][0]+text+self.presuffix[UPNEW][1]

    def match_l(self, list):
        m=[self.match(str) for str in list]
        # print(m)
        return [t for t in m if t]


class GCV:
    def __init__(self,credential):
        self.client = vision.ImageAnnotatorClient.from_service_account_json(credential)

    def image_to_string(self, image_path):
        ret = []
        with open(image_path, 'rb') as fp:
            content = fp.read()
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        if len(response.text_annotations):
            return response.text_annotations[0].description.split("\n")
        return []

