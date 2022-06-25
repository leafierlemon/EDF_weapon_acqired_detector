# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WeaponDetectorGUIwxiGAD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 581)
        MainWindow.setMinimumSize(QSize(800, 0))
        MainWindow.setStyleSheet(u"font: 12pt \"Ricty Diminished Discord\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_output = QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setGeometry(QRect(410, 30, 251, 531))
        font = QFont()
        font.setFamily(u"Ricty Diminished Discord")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        # font.setWeight(50)
        self.textEdit_output.setFont(font)
        self.comboBox_window = QComboBox(self.centralwidget)
        self.comboBox_window.setObjectName(u"comboBox_window")
        self.comboBox_window.setGeometry(QRect(190, 70, 201, 31))
        font1 = QFont()
        font1.setFamily(u"Ricty Diminished Discord")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        # font1.setWeight(50)
        self.comboBox_window.setFont(font1)
        self.comboBox_window.setStyleSheet(u"font: 9pt")
        self.comboBox_window.setEditable(False)
        self.textBrowser_window = QTextBrowser(self.centralwidget)
        self.textBrowser_window.setObjectName(u"textBrowser_window")
        self.textBrowser_window.setGeometry(QRect(30, 70, 161, 31))
        self.textBrowser_window.setFont(font)
        self.pushButton_copyTSV = QPushButton(self.centralwidget)
        self.pushButton_copyTSV.setObjectName(u"pushButton_copyTSV")
        self.pushButton_copyTSV.setGeometry(QRect(660, 250, 141, 61))
        self.pushButton_copyTSV.setFont(font)
        self.pushButton_copyTSV.setStyleSheet(u"")
        self.textBrowser_output = QTextBrowser(self.centralwidget)
        self.textBrowser_output.setObjectName(u"textBrowser_output")
        self.textBrowser_output.setGeometry(QRect(410, 0, 251, 31))
        self.textBrowser_output.setFont(font)
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(660, 500, 141, 61))
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet(u"")
        self.pushButton_scan = QPushButton(self.centralwidget)
        self.pushButton_scan.setObjectName(u"pushButton_scan")
        self.pushButton_scan.setGeometry(QRect(660, 30, 141, 61))
        self.pushButton_scan.setFont(font)
        self.pushButton_scan.setStyleSheet(u"")
        self.textBrowser_upload = QTextBrowser(self.centralwidget)
        self.textBrowser_upload.setObjectName(u"textBrowser_upload")
        self.textBrowser_upload.setGeometry(QRect(30, 360, 331, 192))
        self.textBrowser_upload.setFont(font)
        self.textBrowser_upload.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.textBrowser_title = QTextBrowser(self.centralwidget)
        self.textBrowser_title.setObjectName(u"textBrowser_title")
        self.textBrowser_title.setGeometry(QRect(20, 10, 371, 41))
        self.textBrowser_title.setFont(font)
        self.textBrowser_area = QTextBrowser(self.centralwidget)
        self.textBrowser_area.setObjectName(u"textBrowser_area")
        self.textBrowser_area.setGeometry(QRect(30, 110, 161, 31))
        self.textBrowser_area.setFont(font)
        self.comboBox_area = QComboBox(self.centralwidget)
        self.comboBox_area.setObjectName(u"comboBox_area")
        self.comboBox_area.setGeometry(QRect(190, 110, 201, 31))
        self.comboBox_area.setFont(font)
        self.comboBox_area.setEditable(False)
        self.widget_upload = QWidget(self.centralwidget)
        self.widget_upload.setObjectName(u"widget_upload")
        self.widget_upload.setGeometry(QRect(30, 360, 331, 191))
        self.widget_upload.setAcceptDrops(True)
        self.pushButton_window = QPushButton(self.centralwidget)
        self.pushButton_window.setObjectName(u"pushButton_window")
        self.pushButton_window.setGeometry(QRect(0, 70, 31, 31))
        self.pushButton_window.setMinimumSize(QSize(31, 0))
        self.pushButton_area = QPushButton(self.centralwidget)
        self.pushButton_area.setObjectName(u"pushButton_area")
        self.pushButton_area.setEnabled(False)
        self.pushButton_area.setGeometry(QRect(0, 110, 31, 31))
        self.textBrowser_filter = QTextBrowser(self.centralwidget)
        self.textBrowser_filter.setObjectName(u"textBrowser_filter")
        self.textBrowser_filter.setGeometry(QRect(30, 160, 161, 31))
        self.textBrowser_filter.setFont(font)
        self.comboBox_filter = QComboBox(self.centralwidget)
        self.comboBox_filter.setObjectName(u"comboBox_filter")
        self.comboBox_filter.setGeometry(QRect(190, 160, 201, 31))
        self.comboBox_filter.setFont(font)
        self.comboBox_filter.setEditable(False)
        self.pushButton_filter = QPushButton(self.centralwidget)
        self.pushButton_filter.setObjectName(u"pushButton_filter")
        self.pushButton_filter.setEnabled(False)
        self.pushButton_filter.setGeometry(QRect(0, 160, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WeaponDetector", None))
        self.textBrowser_window.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u30ad\u30e3\u30d7\u30c1\u30e3Window\uff1a</p></body></html>", None))
        self.pushButton_copyTSV.setText(QCoreApplication.translate("MainWindow", u"CopyTSV", None))
        self.textBrowser_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u691c\u51fa\u7d50\u679c</p></body></html>", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.textBrowser_upload.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS UI Gothic'; font-size:9pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To Scan Image</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Drop Here</p></body></html>", None))
        self.textBrowser_title.setDocumentTitle("")
        self.textBrowser_title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">EDF\u30ad\u30e3\u30d7\u30c1\u30e3\u304b\u3089\u6b66\u5668\u3092\u8aad\u307f\u53d6\u308b\u3084\u3064</span></p></body></html>", None))
        self.textBrowser_area.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5bfe\u8c61\u753b\u9762\uff1a</p></body></html>", None))
        self.pushButton_window.setText(QCoreApplication.translate("MainWindow", u"\u27f2", None))
        self.pushButton_area.setText(QCoreApplication.translate("MainWindow", u"\u27f2", None))
        self.textBrowser_filter.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ricty Diminished Discord'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u30d5\u30a3\u30eb\u30bf\u30fc\uff1a</p></body></html>", None))
        self.pushButton_filter.setText(QCoreApplication.translate("MainWindow", u"\u27f2", None))
    # retranslateUi

