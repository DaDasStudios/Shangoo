# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadscreeneZSaqh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 620, 380))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"border-image: url(:/Icons/sprites/background_load.jpg);\n"
"border-radius: 20px;\n"
"border: none;\n"
"}")
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(150, 80, 331, 71))
        font = QFont()
        font.setFamily(u"Nordic Alternative")
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet(u"#title{\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgba(0, 0, 0, 150);\n"
"border: 4px solid white;\n"
"border-radius: 10px;\n"
"}\n"
"#title:hover{\n"
"color: rgba(255, 255, 255, 230);\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)
        self.dark_effect = QLabel(self.widget)
        self.dark_effect.setObjectName(u"dark_effect")
        self.dark_effect.setGeometry(QRect(0, 0, 620, 380))
        self.dark_effect.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 220), stop:0.1875 rgba(0, 0, 0, 200), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 20px;\n"
"")
        self.descp = QLabel(self.widget)
        self.descp.setObjectName(u"descp")
        self.descp.setGeometry(QRect(180, 160, 281, 20))
        font1 = QFont()
        font1.setFamily(u"Aqua Grotesque")
        font1.setPointSize(11)
        font1.setItalic(False)
        self.descp.setFont(font1)
        self.descp.setCursor(QCursor(Qt.ArrowCursor))
        self.descp.setStyleSheet(u"color: white;\n"
"border-bottom: 1px solid white;\n"
"background: transparent;\n"
"border-radius: 2px;")
        self.descp.setAlignment(Qt.AlignCenter)
        self.dark_effect_2 = QLabel(self.widget)
        self.dark_effect_2.setObjectName(u"dark_effect_2")
        self.dark_effect_2.setGeometry(QRect(0, 0, 620, 380))
        font2 = QFont()
        font2.setKerning(True)
        self.dark_effect_2.setFont(font2)
        self.dark_effect_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 160);\n"
"border-radius: 20px;\n"
"border: 5px solid white;")
        self.credits = QLabel(self.widget)
        self.credits.setObjectName(u"credits")
        self.credits.setGeometry(QRect(470, 350, 141, 20))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(8)
        font3.setItalic(True)
        font3.setUnderline(False)
        self.credits.setFont(font3)
        self.credits.setStyleSheet(u"color: rgba(255, 255, 255, 150);\n"
"background-color: transparent;")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 240, 451, 31))
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(True)
        font4.setWeight(50)
        self.progressBar.setFont(font4)
        self.progressBar.setStyleSheet(u"#progressBar{\n"
"border: 2px solid white;\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.511, x2:0, y2:0.506, stop:0 rgba(48, 48, 47, 255), stop:1 rgba(7, 7, 7, 255));\n"
"color: rgba(255, 255, 255,190);\n"
"\n"
"}\n"
"#progressBar:chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.449, x2:1, y2:0.682, stop:0.0227273 rgba(0, 0, 0, 220), stop:1 rgba(20, 20, 20, 220));\n"
"border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.close_button = QPushButton(self.widget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(585, 12, 21, 23))
        font5 = QFont()
        font5.setFamily(u"Arial")
        self.close_button.setFont(font5)
        self.close_button.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"color:rgba(94, 94, 94, 255);\n"
"padding-left: 1px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:  rgba(94, 94, 94, 150);\n"
"border-radius: 8px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/sprites/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.dark_effect.raise_()
        self.dark_effect_2.raise_()
        self.descp.raise_()
        self.title.raise_()
        self.credits.raise_()
        self.progressBar.raise_()
        self.close_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Shangoo", None))
        self.dark_effect.setText("")
        self.descp.setText(QCoreApplication.translate("MainWindow", u"STARTING APP...", None))
        self.dark_effect_2.setText("")
        self.credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Developed By <span style=\" font-weight:600;\">DAS Studios</span></p></body></html>", None))
        self.close_button.setText("")
    # retranslateUi

