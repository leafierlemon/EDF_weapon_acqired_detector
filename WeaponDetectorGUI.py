import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from modules.UI import Ui_MainWindow
from modules.capture import Capture
from modules.detector import Detector
import win32gui
import json
from PIL import Image
import pyclip

MSG = {
    "proc": "Processing: ",
    "error": "Error: ",
    "succ":"Success: "
}
CONFIG_FILE="./config/config.json"

class WeaponDetector(QMainWindow):

    def __init__(self, parent=None):
        super(WeaponDetector, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_scan.clicked.connect(self.scan)
        self.ui.pushButton_copyTSV.clicked.connect(self.copyTSV)
        self.ui.pushButton_clear.clicked.connect(self.clear_o)
        self.ui.textBrowser_upload.setAcceptDrops(True)
        self.ui.widget_upload.dragEnterEvent = self.dragEnter
        self.ui.widget_upload.dropEvent = self.drop
        self.ui.pushButton_window.clicked.connect(self.enumWindow)

        self.l_window = []

        self.enumWindow(None)
        with open(CONFIG_FILE,mode="r",encoding="utf-8") as cf:
            config=json.load(cf)
        self.credential=config["const"]["credential"]
        self.tableDir=config["const"]["tableDir"]
        self.target=config["target"]
        self.ui.comboBox_area.addItems(self.target.keys())
        self.filter=config["filter"]
        self.ui.comboBox_filter.addItems(self.filter.keys())


    # def test(self):
    #     self.showMessage(MSG["proc"])
    #     self.ui.textEdit_output.setText("qwer\nasdf<br/>zxcv")
    #     print(self.ui.textEdit_output.toPlainText())

    def print_o(self, text):
        pre = self.ui.textEdit_output.toPlainText()
        self.ui.textEdit_output.setPlainText(pre+text+"\n")

    def scan(self):
        win_name = self.ui.comboBox_window.currentText()
        setting = self.target[self.ui.comboBox_area.currentText()]
        self.showMessage(MSG["proc"]+"Capture Window")

        self.capture = Capture(win_name)
        img = self.capture.screenshot_client()
        hwnd = win32gui.FindWindow(None, self.windowTitle())
        win32gui.SetForegroundWindow(hwnd)
        if not img:
            self.showMessage(MSG["error"]+"Capture Failed.")
            return

        self.showMessage(MSG["succ"]+"Capture Window")
        self.showMessage(MSG["proc"]+"Detect")
        target=self.target[self.ui.comboBox_area.currentText()]
        filter=self.filter[self.ui.comboBox_filter.currentText()]
        d=Detector(self.tableDir+target["table"],target["trim"],self.credential,filter=filter)

        o=d.do(img)

        self.print_o("\n".join(o))
        del d
        self.showMessage(MSG["succ"]+"Detect")
        return

    def copyTSV(self):
        self.showMessage(MSG["proc"])
        pyclip.copy(self.ui.textEdit_output.toPlainText().replace("\n","\t"))
        self.showMessage(MSG["succ"]+"Copy to Clipboad.")
        return

    def clear_o(self):
        self.ui.textEdit_output.setPlainText("")
        return

    def dragEnter(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        return

    def drop(self, e):
        self.showMessage(MSG["proc"]+"Drop")
        target=self.target[self.ui.comboBox_area.currentText()]
        filter=self.filter[self.ui.comboBox_filter.currentText()]
        d=Detector(self.tableDir+target["table"],target["trim"],self.credential,filter=filter)
        for url in e.mimeData().urls():
            img=Image.open(url.toLocalFile())
            o=d.do(img)
            # print(o)
            self.print_o("\n".join(o))
        del d
        self.showMessage(MSG["succ"]+"Drop")

    def enumWindow(self, e):
        self.showMessage(MSG["proc"]+"EnumWindow")
        # self.ui.textEdit_output.setText("enum")
        o = []

        def _callback(hwnd, o):
            o.append(hwnd)
        win32gui.EnumWindows(_callback, o)

        while self.ui.comboBox_window.count():
            self.ui.comboBox_window.removeItem(0)
        o2 = [win32gui.GetWindowText(h) for h in o]
        self.ui.comboBox_window.addItems([t for t in o2 if t])
        self.showMessage(MSG["succ"]+"EnumWindow")

    def showMessage(self, str):
        self.ui.statusBar.showMessage(str)

    
#     def clear_output(self):
#         return
#     def clear_output(self):
#         return

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = WeaponDetector()
#     window.show()
#     sys.exit(app.exec_())


def main() -> None:
    app = QApplication(sys.argv)
    window = WeaponDetector()
#     window.setCentralWidget(QWidget())
#     central_widget = window.centralWidget()     # この行を追加
#     central_widget.setLayout(QVBoxLayout())
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
