import cv2
import argparse
import os
import numpy as np
import difflib
from google.cloud import vision

parser = argparse.ArgumentParser()
parser.add_argument('images', metavar='file', type=str, nargs='+',
                    help='input image files(1920x1080でのみテスト)')
parser.add_argument("--threshold","-th", type=int, choices=range(0,256),default=146, help="2値化の閾値(0~255)")
parser.add_argument("--table","-t", default="./data/EDF5_WEAPON_LIST_JA.txt", help="マッチ検索する武器名テーブルファイル")
parser.add_argument("--credentials","-c", required=True, help="Google Vision API用の認証情報(json)")

args = parser.parse_args()

def main():
    d=[]
    # ファイルかを判定
    for f in args.images:
        if os.path.isfile(f):
            d.append(f)
        elif os.path.isdir(f):
            d.extend([f+'/'+a for a in os.listdir(f)])
        else:
            print('Input file "%s" in not file or directory.'%f)
            return
    m=Matcher(args.table)
    ocr=OCR()
    for img_path in d:
        print("trim...")
        t=trim(img_path)

        print("ocr...")
        ocr_result=ocr.image_to_string(t)
        # print(ocr_result)

        print("match...")
        o=[]
        for r in ocr_result:
            out=m.match(r)
            # print(r+": ",end="")
            if len(out):
                o.append(out[0])
        print("\n".join(o))
        with open('./out.txt', mode='a',encoding="utf-8") as f:
            f.write("\t".join(o)+"\n")
            

def trim(img_path):
    t=[]
    img=cv2.imread(img_path)
    basename, extention = os.path.splitext(os.path.basename(img_path))

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,img_bin=cv2.threshold(gray,args.threshold,255,cv2.THRESH_BINARY_INV)
    HEIGHT=len(img)
    WIDTH=len(img[0])

    selected=[WIDTH*852//1920,HEIGHT*268//1080,WIDTH*454//1920,HEIGHT*568//1080]

    
    if sum(selected):
        img_bin_tr = img_bin[int(selected[1]):int(selected[1]+selected[3]),
                        int(selected[0]):int(selected[0]+selected[2])]
        img_bin=img_bin_tr

    outfile="./tmp/"+basename+"_bin"+extention
    cv2.imwrite(outfile, img_bin)
    return outfile

class Matcher:
    def __init__(self, table):
        with open(table,encoding='utf-8')as f:
           self.table=f.read().splitlines()

    def match(self,str):
        o=[]
        for w in self.table:
            o.append(difflib.SequenceMatcher(None,str,w).ratio())
        ih=np.argsort(o)[::-1]
        th=0.5
        th_diff=max(o)-0.05
        return [self.table[i] for i in ih if (o[i]>th and o[i] > th_diff)]

class OCR:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient.from_service_account_json(args.credentials)

    def image_to_string(self,image_path):
        ret=[]
        with open(image_path, 'rb') as fp:
            content = fp.read()
        image = vision.Image(content=content)
        response = self.client.text_detection(image=image)
        return response.text_annotations[0].description.split("\n")


if __name__ == '__main__':
    main()