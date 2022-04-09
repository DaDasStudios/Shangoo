# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screen_uigEBLBf.ui'
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
        MainWindow.resize(1180, 733)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"#body {\n"
"background-color: #ffffff;border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu_container = QFrame(self.body)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMinimumSize(QSize(0, 0))
        self.side_menu_container.setMaximumSize(QSize(250, 16777215))
        self.side_menu_container.setStyleSheet(u"")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.side_menu_container)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"\n"
"#header{\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"}\n"
"#header:hover{\n"
"background-color: #e8e8e8;\n"
"}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.header)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        font = QFont()
        font.setFamily(u"Nordic Alternative")
        font.setPointSize(25)
        self.logo.setFont(font)
        self.logo.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgb(63, 63, 63);\n"
"border: 4px solid white;\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.logo)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignTop)

        self.options_frame = QFrame(self.side_menu_container)
        self.options_frame.setObjectName(u"options_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.options_frame.sizePolicy().hasHeightForWidth())
        self.options_frame.setSizePolicy(sizePolicy)
        self.options_frame.setMinimumSize(QSize(0, 0))
        self.options_frame.setStyleSheet(u"\n"
"#options_frame {\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.options_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.options_btns_frame = QFrame(self.options_frame)
        self.options_btns_frame.setObjectName(u"options_btns_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.options_btns_frame.sizePolicy().hasHeightForWidth())
        self.options_btns_frame.setSizePolicy(sizePolicy1)
        self.options_btns_frame.setMinimumSize(QSize(0, 0))
        self.options_btns_frame.setMaximumSize(QSize(300, 16777215))
        self.options_btns_frame.setStyleSheet(u"#options_btns_frame {\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 10px;\n"
"background-color: #ffffff;\n"
"text-align: right;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #e8e8e8;\n"
"}\n"
"\n"
"* {\n"
"font: 16px \"Roboto\";\n"
"	color:#393939;\n"
"}\n"
"")
        self.options_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.options_btns_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.options_btns_frame)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(5, 5, 5, 5)
        self.setting_button = QPushButton(self.options_btns_frame)
        self.setting_button.setObjectName(u"setting_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setting_button.sizePolicy().hasHeightForWidth())
        self.setting_button.setSizePolicy(sizePolicy2)
        self.setting_button.setMinimumSize(QSize(200, 60))
        self.setting_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_button.setLayoutDirection(Qt.LeftToRight)
        self.setting_button.setStyleSheet(u"#setting_button{\n"
"	image: url(:/Icons/sprites/icons/config.png);\n"
"	image-position: left;\n"
"	padding: 10px;\n"
"	padding-right:40px;\n"
"	padding-left: 20px;\n"
"}")
        self.setting_button.setIconSize(QSize(35, 35))

        self.verticalLayout_42.addWidget(self.setting_button)

        self.media_button = QPushButton(self.options_btns_frame)
        self.media_button.setObjectName(u"media_button")
        sizePolicy2.setHeightForWidth(self.media_button.sizePolicy().hasHeightForWidth())
        self.media_button.setSizePolicy(sizePolicy2)
        self.media_button.setMinimumSize(QSize(0, 60))
        self.media_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.media_button.setStyleSheet(u"#media_button{\n"
"	image: url(:/Icons/sprites/icons/social.png);\n"
"	image-position: left;\n"
"	padding: 10px;\n"
"	padding-right:20px;\n"
"	padding-left: 20px;\n"
"}")
        self.media_button.setIconSize(QSize(35, 35))

        self.verticalLayout_42.addWidget(self.media_button)

        self.about_us_button = QPushButton(self.options_btns_frame)
        self.about_us_button.setObjectName(u"about_us_button")
        sizePolicy2.setHeightForWidth(self.about_us_button.sizePolicy().hasHeightForWidth())
        self.about_us_button.setSizePolicy(sizePolicy2)
        self.about_us_button.setMinimumSize(QSize(0, 60))
        self.about_us_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_us_button.setFocusPolicy(Qt.NoFocus)
        self.about_us_button.setLayoutDirection(Qt.LeftToRight)
        self.about_us_button.setStyleSheet(u"#about_us_button{\n"
"	\n"
"	image: url(:/Icons/sprites/icons/web.png);\n"
"	image-position: left;\n"
"	padding: 10px;\n"
"	padding-right:40px;\n"
"	padding-left: 20px;\n"
"}")
        self.about_us_button.setIconSize(QSize(35, 35))

        self.verticalLayout_42.addWidget(self.about_us_button)

        self.help_button = QPushButton(self.options_btns_frame)
        self.help_button.setObjectName(u"help_button")
        sizePolicy2.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy2)
        self.help_button.setMinimumSize(QSize(0, 60))
        self.help_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.help_button.setStyleSheet(u"#help_button{	\n"
"	image: url(:/Icons/sprites/icons/help.png);\n"
"	image-position: left;\n"
"	padding: 10px;\n"
"	padding-right:55px;\n"
"	padding-left: 20px;\n"
"}")
        self.help_button.setIconSize(QSize(35, 35))

        self.verticalLayout_42.addWidget(self.help_button)


        self.verticalLayout_4.addWidget(self.options_btns_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.content_menu = QStackedWidget(self.options_frame)
        self.content_menu.setObjectName(u"content_menu")
        self.content_menu.setMinimumSize(QSize(0, 300))
        self.content_menu.setStyleSheet(u"#content_menu{\n"
"background-color: #efefef;\n"
"}\n"
"#content_menu QTabBar::scroller{\n"
"color:red;\n"
"}\n"
"#content_menu QTabBar::tab{\n"
"font: 10px \"Roboto\";\n"
"color:#393939;\n"
"padding: 5px;\n"
"text-align: center;\n"
"margin-top: 5px;\n"
"margin-left: 5.5px;\n"
"border: none;\n"
"border-radius: 3px;\n"
"}\n"
"#content_menu QTabBar::tab:hover{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"#content_menu QTabBar::tab:selected{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"")
        self.content_menu.setFrameShape(QFrame.StyledPanel)
        self.content_menu.setFrameShadow(QFrame.Raised)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_6 = QVBoxLayout(self.Settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.settings_tab = QTabWidget(self.Settings)
        self.settings_tab.setObjectName(u"settings_tab")
        self.settings_tab.setMaximumSize(QSize(16777, 350))
        self.settings_tab.setCursor(QCursor(Qt.ArrowCursor))
        self.settings_tab.setStyleSheet(u"\n"
"QWidget {\n"
"background-color: #e8e8e8;\n"
"border-radius: 5px;\n"
"selection-background-color: #efefef;\n"
"selection-color: #AFAFAF;\n"
"}\n"
"\n"
"/* BUTTONS */\n"
"\n"
"QPushButton{\n"
"font: 12px \"Roboto\";\n"
"color:#393939;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"margin: 3px;\n"
"padding-top: 7px;\n"
"padding-bottom: 7px;\n"
"text-align: center;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
" \n"
"/* QLABELS */\n"
"\n"
"QLabel{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 12px \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 7px;\n"
"margin-top: 0.7em;\n"
"margin-bottom: 3px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: #393939;\n"
"}")
        self.settings_tab.setTabPosition(QTabWidget.North)
        self.settings_tab.setTabShape(QTabWidget.Rounded)
        self.settings_tab.setElideMode(Qt.ElideNone)
        self.settings_tab.setUsesScrollButtons(False)
        self.settings_tab.setMovable(True)
        self.language = QWidget()
        self.language.setObjectName(u"language")
        self.verticalLayout_9 = QVBoxLayout(self.language)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.language_list = QListWidget(self.language)
        self.language_list.setObjectName(u"language_list")
        self.language_list.setStyleSheet(u"#language_list{\n"
"background-color: white;\n"
"selection-background-color: rgb(85, 255, 255);\n"
"margin-top: 5px;\n"
"margin-bottom: 3px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"padding: 1em;\n"
"font: 14px \"Roboto\";\n"
"color: #393939;\n"
"}\n"
"#language_list::item{\n"
"padding: 3px 3px 3px 3px;\n"
"padding-bottom: 3px;\n"
"margin-bottom: 0.5em;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"#language_list::item:hover{\n"
"background-color: #efefef;\n"
"padding-left:2px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"#language_list::item:selected{\n"
"text-decoration: none;\n"
"background-color: #E0E0E0;\n"
"color: #393939;\n"
"padding-left:7px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"#language_list:focus{\n"
"border: none;\n"
"outline: none;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.language_list)

        self.apply_btn = QPushButton(self.language)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.apply_btn.setStyleSheet(u"image: url(:/Icons/sprites/icons/save.png);\n"
"image-position: left;\n"
"padding-left: 25%;\n"
"padding-right: 18%")

        self.verticalLayout_9.addWidget(self.apply_btn)

        self.settings_tab.addTab(self.language, "")
        self.units = QWidget()
        self.units.setObjectName(u"units")
        self.units.setStyleSheet(u"QComboBox{\n"
"background-color: white;\n"
"color: #393939;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"font: 12px \"Roboto\";\n"
"}\n"
"QComboBox::drop-down{\n"
"background: #E5E5E5;\n"
"color: #AFAFAF;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"QComboBox::drop-down:hover{\n"
"background: #C3C2C2;\n"
"color: white;\n"
"}\n"
"QComboBox::drop-down:on{\n"
"background: #AFAFAF;\n"
"}\n"
"/* POPUP ELEMENTS */\n"
"QComboBox QAbstractItemView {\n"
"background: white;\n"
"selection-background-color: #E5E5E5;\n"
"selection-color: #393939;\n"
"border: none;\n"
"outline: none;\n"
"font: 12px \"Roboto\";\n"
"color: #393939;\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.units)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.units_frame = QFrame(self.units)
        self.units_frame.setObjectName(u"units_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.units_frame.sizePolicy().hasHeightForWidth())
        self.units_frame.setSizePolicy(sizePolicy3)
        self.units_frame.setMinimumSize(QSize(0, 300))
        self.units_frame.setFrameShape(QFrame.StyledPanel)
        self.units_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.units_frame)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.units_frame_content = QFrame(self.units_frame)
        self.units_frame_content.setObjectName(u"units_frame_content")
        self.units_frame_content.setFrameShape(QFrame.StyledPanel)
        self.units_frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.units_frame_content)
        self.verticalLayout_46.setSpacing(10)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.angle_title = QLabel(self.units_frame_content)
        self.angle_title.setObjectName(u"angle_title")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.angle_title.sizePolicy().hasHeightForWidth())
        self.angle_title.setSizePolicy(sizePolicy4)
        self.angle_title.setMinimumSize(QSize(0, 25))
        self.angle_title.setStyleSheet(u"")
        self.angle_title.setAlignment(Qt.AlignCenter)
        self.angle_title.setWordWrap(True)
        self.angle_title.setMargin(5)

        self.verticalLayout_46.addWidget(self.angle_title)

        self.angle_comboBox = QComboBox(self.units_frame_content)
        self.angle_comboBox.addItem("")
        self.angle_comboBox.addItem("")
        self.angle_comboBox.addItem("")
        self.angle_comboBox.setObjectName(u"angle_comboBox")
        self.angle_comboBox.setMinimumSize(QSize(0, 30))
        self.angle_comboBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_46.addWidget(self.angle_comboBox)


        self.verticalLayout_11.addWidget(self.units_frame_content, 0, Qt.AlignTop)

        self.apply_angle = QPushButton(self.units_frame)
        self.apply_angle.setObjectName(u"apply_angle")
        self.apply_angle.setMinimumSize(QSize(0, 30))
        self.apply_angle.setCursor(QCursor(Qt.ArrowCursor))
        self.apply_angle.setStyleSheet(u"image: url(:/Icons/sprites/icons/save.png);\n"
"image-position: left;\n"
"padding-left: 25%;\n"
"padding-right: 18%")
        self.apply_angle.setIconSize(QSize(16, 16))

        self.verticalLayout_11.addWidget(self.apply_angle, 0, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.units_frame, 0, Qt.AlignTop)

        self.settings_tab.addTab(self.units, "")
        self.macros = QWidget()
        self.macros.setObjectName(u"macros")
        self.verticalLayout_12 = QVBoxLayout(self.macros)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.macros_frame = QFrame(self.macros)
        self.macros_frame.setObjectName(u"macros_frame")
        self.macros_frame.setFrameShape(QFrame.StyledPanel)
        self.macros_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.macros_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.macro_title = QLabel(self.macros_frame)
        self.macro_title.setObjectName(u"macro_title")
        self.macro_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.macro_title)

        self.macros_table_frame = QFrame(self.macros_frame)
        self.macros_table_frame.setObjectName(u"macros_table_frame")
        self.macros_table_frame.setStyleSheet(u"QFrame{\n"
"background-color: #ffffff;\n"
"border-radius: 10px;\n"
"}")
        self.macros_table_frame.setFrameShape(QFrame.StyledPanel)
        self.macros_table_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.macros_table_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 1)
        self.macros_table_widget = QTableWidget(self.macros_table_frame)
        if (self.macros_table_widget.columnCount() < 1):
            self.macros_table_widget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.macros_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.macros_table_widget.rowCount() < 5):
            self.macros_table_widget.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.macros_table_widget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.macros_table_widget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.macros_table_widget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.macros_table_widget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.macros_table_widget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.macros_table_widget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.macros_table_widget.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.macros_table_widget.setItem(2, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.macros_table_widget.setItem(3, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.macros_table_widget.setItem(4, 0, __qtablewidgetitem10)
        self.macros_table_widget.setObjectName(u"macros_table_widget")
        self.macros_table_widget.setMinimumSize(QSize(0, 0))
        self.macros_table_widget.setLayoutDirection(Qt.LeftToRight)
        self.macros_table_widget.setAutoFillBackground(False)
        self.macros_table_widget.setStyleSheet(u"QTableWidget{\n"
"background-color: white;\n"
"color: #393939;\n"
"outline: none;\n"
"font: 12px \"Roboto\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTableWidget::item:hover{\n"
"background-color: #efefef;\n"
"padding-left:2px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"background-color: #E0E0E0;\n"
"color: #393939;\n"
"padding-left:7px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"font: 12px \"Roboto\";\n"
"color: #393939;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section{\n"
"background-color: white;\n"
"border: none;\n"
"padding-left: 5px;\n"
"color: #393939;\n"
"}\n"
"QTableWidget QHeaderView::section:hover{\n"
"background: #E5E5E5;\n"
"padding-left:2px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"QTableWidget QHeaderView::section:checked{\n"
"background-color: #E0E0E0;\n"
"font: 10pt \"Roboto\";\n"
"color: #393939;\n"
""
                        "padding-left:7px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}")
        self.macros_table_widget.setFrameShape(QFrame.NoFrame)
        self.macros_table_widget.setFrameShadow(QFrame.Plain)
        self.macros_table_widget.setLineWidth(0)
        self.macros_table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.macros_table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.macros_table_widget.setAutoScrollMargin(16)
        self.macros_table_widget.setAlternatingRowColors(False)
        self.macros_table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.macros_table_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.macros_table_widget.setShowGrid(True)
        self.macros_table_widget.setGridStyle(Qt.SolidLine)
        self.macros_table_widget.setSortingEnabled(False)
        self.macros_table_widget.horizontalHeader().setVisible(False)
        self.macros_table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.macros_table_widget.horizontalHeader().setProperty("showSortIndicator", False)
        self.macros_table_widget.horizontalHeader().setStretchLastSection(True)
        self.macros_table_widget.verticalHeader().setMinimumSectionSize(23)
        self.macros_table_widget.verticalHeader().setDefaultSectionSize(35)
        self.macros_table_widget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_13.addWidget(self.macros_table_widget)


        self.verticalLayout_13.addWidget(self.macros_table_frame)

        self.frame_macros_btns = QFrame(self.macros_frame)
        self.frame_macros_btns.setObjectName(u"frame_macros_btns")
        self.frame_macros_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_macros_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_macros_btns)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.save_macros_btn = QPushButton(self.frame_macros_btns)
        self.save_macros_btn.setObjectName(u"save_macros_btn")
        self.save_macros_btn.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_9.addWidget(self.save_macros_btn)

        self.reset_macros_btn = QPushButton(self.frame_macros_btns)
        self.reset_macros_btn.setObjectName(u"reset_macros_btn")
        self.reset_macros_btn.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_9.addWidget(self.reset_macros_btn)


        self.verticalLayout_13.addWidget(self.frame_macros_btns)


        self.verticalLayout_12.addWidget(self.macros_frame)

        self.use_macro_selected = QPushButton(self.macros)
        self.use_macro_selected.setObjectName(u"use_macro_selected")
        self.use_macro_selected.setCursor(QCursor(Qt.ArrowCursor))
        self.use_macro_selected.setStyleSheet(u"image: url(:/Icons/sprites/icons/hand.png);\n"
"image-position: left;\n"
"padding-left: 25%;\n"
"padding-right: 18%")

        self.verticalLayout_12.addWidget(self.use_macro_selected)

        self.settings_tab.addTab(self.macros, "")
        self.preferences_tab = QWidget()
        self.preferences_tab.setObjectName(u"preferences_tab")
        self.verticalLayout_39 = QVBoxLayout(self.preferences_tab)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.preferences_frame = QFrame(self.preferences_tab)
        self.preferences_frame.setObjectName(u"preferences_frame")
        self.preferences_frame.setFrameShape(QFrame.StyledPanel)
        self.preferences_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.preferences_frame)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.preferences_title = QLabel(self.preferences_frame)
        self.preferences_title.setObjectName(u"preferences_title")
        self.preferences_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.preferences_title, 0, Qt.AlignTop)

        self.preferences_container_frame = QFrame(self.preferences_frame)
        self.preferences_container_frame.setObjectName(u"preferences_container_frame")
        sizePolicy3.setHeightForWidth(self.preferences_container_frame.sizePolicy().hasHeightForWidth())
        self.preferences_container_frame.setSizePolicy(sizePolicy3)
        self.preferences_container_frame.setStyleSheet(u"#preferences_container_frame{\n"
"background-color: #FFF;\n"
"margin: 5px;\n"
"}\n"
"\n"
"QCheckBox{\n"
"background-color: #FFF;\n"
"color: #393939;\n"
"font: 9pt \"Roboto\";\n"
"padding: 5px;\n"
"}\n"
"\n"
"QCheckBox:hover{\n"
"background-color: #efefef;\n"
"padding-left:2px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}\n"
"\n"
"QCheckBox:checked{\n"
"text-decoration: none;\n"
"background-color: #E0E0E0;\n"
"color: #393939;\n"
"padding-left:7px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"}")
        self.preferences_container_frame.setFrameShape(QFrame.StyledPanel)
        self.preferences_container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.preferences_container_frame)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(20, 9, 9, 9)
        self.logy_checkbox = QCheckBox(self.preferences_container_frame)
        self.logy_checkbox.setObjectName(u"logy_checkbox")
        self.logy_checkbox.setIconSize(QSize(5, 16))
        self.logy_checkbox.setChecked(True)
        self.logy_checkbox.setTristate(False)

        self.verticalLayout_45.addWidget(self.logy_checkbox)

        self.loadscreen_checkbox = QCheckBox(self.preferences_container_frame)
        self.loadscreen_checkbox.setObjectName(u"loadscreen_checkbox")
        self.loadscreen_checkbox.setChecked(True)

        self.verticalLayout_45.addWidget(self.loadscreen_checkbox)

        self.menu_checkbox = QCheckBox(self.preferences_container_frame)
        self.menu_checkbox.setObjectName(u"menu_checkbox")
        self.menu_checkbox.setChecked(True)

        self.verticalLayout_45.addWidget(self.menu_checkbox)


        self.verticalLayout_40.addWidget(self.preferences_container_frame)

        self.preferences_apply = QPushButton(self.preferences_frame)
        self.preferences_apply.setObjectName(u"preferences_apply")
        self.preferences_apply.setCursor(QCursor(Qt.ArrowCursor))
        self.preferences_apply.setStyleSheet(u"image: url(:/Icons/sprites/icons/save.png);\n"
"image-position: left;\n"
"padding-left: 25%;\n"
"padding-right: 18%")

        self.verticalLayout_40.addWidget(self.preferences_apply)


        self.verticalLayout_39.addWidget(self.preferences_frame)

        self.settings_tab.addTab(self.preferences_tab, "")

        self.verticalLayout_6.addWidget(self.settings_tab, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.content_menu.addWidget(self.Settings)
        self.SocialMedia = QWidget()
        self.SocialMedia.setObjectName(u"SocialMedia")
        self.SocialMedia.setStyleSheet(u"\n"
"#SocialMedia QPushButton{\n"
"font: 12px \"Roboto\";\n"
"color:#393939;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-top: 7px;\n"
"padding-bottom: 7px;\n"
"text-align: center;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"#SocialMedia QPushButton:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.SocialMedia)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.socialmedia = QFrame(self.SocialMedia)
        self.socialmedia.setObjectName(u"socialmedia")
        self.socialmedia.setFrameShape(QFrame.StyledPanel)
        self.socialmedia.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.socialmedia)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.social_title_frame = QFrame(self.socialmedia)
        self.social_title_frame.setObjectName(u"social_title_frame")
        self.social_title_frame.setStyleSheet(u"QFrame {\n"
"background-color: #e8e8e8;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.social_title_frame.setFrameShape(QFrame.StyledPanel)
        self.social_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.social_title_frame)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.social_title = QLabel(self.social_title_frame)
        self.social_title.setObjectName(u"social_title")
        self.social_title.setStyleSheet(u"#social_title{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 12pt \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 7px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"\n"
"\n"
"}\n"
"\n"
"#social_title:hover{\n"
"color: #393939;\n"
"}")
        self.social_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.social_title)


        self.verticalLayout_7.addWidget(self.social_title_frame)

        self.socialmedia_frame = QFrame(self.socialmedia)
        self.socialmedia_frame.setObjectName(u"socialmedia_frame")
        sizePolicy3.setHeightForWidth(self.socialmedia_frame.sizePolicy().hasHeightForWidth())
        self.socialmedia_frame.setSizePolicy(sizePolicy3)
        self.socialmedia_frame.setStyleSheet(u"QFrame {\n"
"margin-top: 5px;\n"
"background-color: #e8e8e8;\n"
"border-radius: 10px;\n"
"}")
        self.socialmedia_frame.setFrameShape(QFrame.StyledPanel)
        self.socialmedia_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.socialmedia_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.facebook_btn = QPushButton(self.socialmedia_frame)
        self.facebook_btn.setObjectName(u"facebook_btn")
        sizePolicy2.setHeightForWidth(self.facebook_btn.sizePolicy().hasHeightForWidth())
        self.facebook_btn.setSizePolicy(sizePolicy2)
        self.facebook_btn.setMinimumSize(QSize(0, 0))
        self.facebook_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.facebook_btn.setStyleSheet(u"image: url(:/Icons/sprites/icons/facebook.svg);\n"
"image-position: left;\n"
"padding-left: 20px;")
        self.facebook_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_41.addWidget(self.facebook_btn)

        self.youtube_btn = QPushButton(self.socialmedia_frame)
        self.youtube_btn.setObjectName(u"youtube_btn")
        sizePolicy2.setHeightForWidth(self.youtube_btn.sizePolicy().hasHeightForWidth())
        self.youtube_btn.setSizePolicy(sizePolicy2)
        self.youtube_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.youtube_btn.setStyleSheet(u"image: url(:/Icons/sprites/icons/youtube.svg);\n"
"image-position: left;\n"
"padding-left: 20px;")
        self.youtube_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_41.addWidget(self.youtube_btn)

        self.instagram_btn = QPushButton(self.socialmedia_frame)
        self.instagram_btn.setObjectName(u"instagram_btn")
        sizePolicy2.setHeightForWidth(self.instagram_btn.sizePolicy().hasHeightForWidth())
        self.instagram_btn.setSizePolicy(sizePolicy2)
        self.instagram_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.instagram_btn.setStyleSheet(u"image: url(:/Icons/sprites/icons/instagram.svg);\n"
"image-position: left;\n"
"padding-left: 20px;")
        self.instagram_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_41.addWidget(self.instagram_btn)

        self.webpage_btn = QPushButton(self.socialmedia_frame)
        self.webpage_btn.setObjectName(u"webpage_btn")
        sizePolicy2.setHeightForWidth(self.webpage_btn.sizePolicy().hasHeightForWidth())
        self.webpage_btn.setSizePolicy(sizePolicy2)
        self.webpage_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.webpage_btn.setStyleSheet(u"image: url(:/Icons/sprites/icons/web.png);\n"
"image-position: left;\n"
"padding-left: 20px;")
        self.webpage_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_41.addWidget(self.webpage_btn)


        self.verticalLayout_7.addWidget(self.socialmedia_frame)


        self.horizontalLayout_7.addWidget(self.socialmedia)

        self.content_menu.addWidget(self.SocialMedia)
        self.Help = QWidget()
        self.Help.setObjectName(u"Help")
        self.Help.setStyleSheet(u"#Help QScrollArea{\n"
"margin: 0px 5px 5px 0;\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"        /* VERTICAL SCROLL */\n"
"\n"
"QScrollBar:vertical {\n"
"background: white;\n"
"width: 1em;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:rgb(195, 194, 194);\n"
"border-radius: 3px;\n"
"width: 0px;\n"
"position: absolute;\n"
"}\n"
"\n"
"/* CONTENT ON LABELS */\n"
"\n"
"#Help QScrollArea QLabel{\n"
"font: 12pt \"Roboto\";\n"
"color: #2B2B2B;\n"
"padding:5px;\n"
"margin-top: 5px;\n"
"selection-background-color: #efefef;\n"
"selection-color: #AFAFAF;\n"
"}\n"
"\n"
"\n"
" /* TABS BOTTOM */\n"
"\n"
"#Help QTabBar::tab{\n"
"font: 10px \"Roboto\";\n"
"color:#393939;\n"
"padding: 5px;\n"
"text-align: center;\n"
"margin-top: 5px;\n"
"border: none;\n"
"}\n"
"#Help QTabBar::tab:hover{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.Help)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.help_frame = QFrame(self.Help)
        self.help_frame.setObjectName(u"help_frame")
        self.help_frame.setStyleSheet(u"")
        self.help_frame.setFrameShape(QFrame.StyledPanel)
        self.help_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.help_frame)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.help_title_frame = QFrame(self.help_frame)
        self.help_title_frame.setObjectName(u"help_title_frame")
        self.help_title_frame.setStyleSheet(u"QFrame {\n"
"background-color: #e8e8e8;\n"
"border-radius: 10px;\n"
"}")
        self.help_title_frame.setFrameShape(QFrame.StyledPanel)
        self.help_title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.help_title_frame)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 5)
        self.help_title = QLabel(self.help_title_frame)
        self.help_title.setObjectName(u"help_title")
        self.help_title.setStyleSheet(u"#help_title{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 12pt \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"margin-top: 5px;\n"
"}\n"
"\n"
"#help_title:hover{\n"
"color: #393939;\n"
"}")
        self.help_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.help_title)


        self.verticalLayout_8.addWidget(self.help_title_frame)

        self.help_tab_widgets = QTabWidget(self.help_frame)
        self.help_tab_widgets.setObjectName(u"help_tab_widgets")
        self.help_tab_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.help_tab_widgets.setStyleSheet(u"\n"
"QWidget{\n"
"background-color: #e8e8e8;\n"
"border-radius: 5px;\n"
"}\n"
"QScrollArea QLabel{\n"
"background-color: white;\n"
"}\n"
"\n"
"")
        self.help_tab_widgets.setTabPosition(QTabWidget.South)
        self.help_tab_widgets.setTabShape(QTabWidget.Rounded)
        self.help_tab_widgets.setElideMode(Qt.ElideNone)
        self.help_tab_widgets.setUsesScrollButtons(False)
        self.help_tab_widgets.setDocumentMode(True)
        self.help_tab_widgets.setTabsClosable(False)
        self.help_tab_widgets.setMovable(True)
        self.help_tab_widgets.setTabBarAutoHide(False)
        self.useful_help_tab = QWidget()
        self.useful_help_tab.setObjectName(u"useful_help_tab")
        self.verticalLayout_29 = QVBoxLayout(self.useful_help_tab)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_useful_help = QScrollArea(self.useful_help_tab)
        self.scrollArea_useful_help.setObjectName(u"scrollArea_useful_help")
        self.scrollArea_useful_help.setStyleSheet(u"")
        self.scrollArea_useful_help.setWidgetResizable(True)
        self.scrollArea_useful_help_frame = QWidget()
        self.scrollArea_useful_help_frame.setObjectName(u"scrollArea_useful_help_frame")
        self.scrollArea_useful_help_frame.setGeometry(QRect(0, 0, 208, 997))
        self.verticalLayout_30 = QVBoxLayout(self.scrollArea_useful_help_frame)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.help_useful_label = QLabel(self.scrollArea_useful_help_frame)
        self.help_useful_label.setObjectName(u"help_useful_label")
        self.help_useful_label.setStyleSheet(u"")
        self.help_useful_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_useful_label.setWordWrap(True)
        self.help_useful_label.setMargin(0)
        self.help_useful_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_30.addWidget(self.help_useful_label)

        self.scrollArea_useful_help.setWidget(self.scrollArea_useful_help_frame)

        self.verticalLayout_29.addWidget(self.scrollArea_useful_help)

        self.help_tab_widgets.addTab(self.useful_help_tab, "")
        self.calculator_help_tab = QWidget()
        self.calculator_help_tab.setObjectName(u"calculator_help_tab")
        self.verticalLayout_32 = QVBoxLayout(self.calculator_help_tab)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_calculator_help = QScrollArea(self.calculator_help_tab)
        self.scrollArea_calculator_help.setObjectName(u"scrollArea_calculator_help")
        self.scrollArea_calculator_help.setWidgetResizable(True)
        self.scrollArea_calculator_help_frame = QWidget()
        self.scrollArea_calculator_help_frame.setObjectName(u"scrollArea_calculator_help_frame")
        self.scrollArea_calculator_help_frame.setGeometry(QRect(0, 0, 208, 3236))
        self.verticalLayout_31 = QVBoxLayout(self.scrollArea_calculator_help_frame)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.help_calculator_label = QLabel(self.scrollArea_calculator_help_frame)
        self.help_calculator_label.setObjectName(u"help_calculator_label")
        self.help_calculator_label.setStyleSheet(u"")
        self.help_calculator_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_calculator_label.setWordWrap(True)
        self.help_calculator_label.setMargin(0)
        self.help_calculator_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_31.addWidget(self.help_calculator_label)

        self.scrollArea_calculator_help.setWidget(self.scrollArea_calculator_help_frame)

        self.verticalLayout_32.addWidget(self.scrollArea_calculator_help)

        self.help_tab_widgets.addTab(self.calculator_help_tab, "")
        self.manual_help_tab = QWidget()
        self.manual_help_tab.setObjectName(u"manual_help_tab")
        self.verticalLayout_36 = QVBoxLayout(self.manual_help_tab)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_manual_help = QScrollArea(self.manual_help_tab)
        self.scrollArea_manual_help.setObjectName(u"scrollArea_manual_help")
        self.scrollArea_manual_help.setWidgetResizable(True)
        self.scrollArea_manual_help_frame = QWidget()
        self.scrollArea_manual_help_frame.setObjectName(u"scrollArea_manual_help_frame")
        self.scrollArea_manual_help_frame.setGeometry(QRect(0, 0, 208, 541))
        self.verticalLayout_33 = QVBoxLayout(self.scrollArea_manual_help_frame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.help_manual_label = QLabel(self.scrollArea_manual_help_frame)
        self.help_manual_label.setObjectName(u"help_manual_label")
        self.help_manual_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_manual_label.setWordWrap(True)
        self.help_manual_label.setMargin(0)
        self.help_manual_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_33.addWidget(self.help_manual_label)

        self.scrollArea_manual_help.setWidget(self.scrollArea_manual_help_frame)

        self.verticalLayout_36.addWidget(self.scrollArea_manual_help)

        self.help_tab_widgets.addTab(self.manual_help_tab, "")
        self.conversions_help_tab = QWidget()
        self.conversions_help_tab.setObjectName(u"conversions_help_tab")
        self.verticalLayout_37 = QVBoxLayout(self.conversions_help_tab)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_convertions_help = QScrollArea(self.conversions_help_tab)
        self.scrollArea_convertions_help.setObjectName(u"scrollArea_convertions_help")
        self.scrollArea_convertions_help.setWidgetResizable(True)
        self.scrollArea_convertions_help_frame = QWidget()
        self.scrollArea_convertions_help_frame.setObjectName(u"scrollArea_convertions_help_frame")
        self.scrollArea_convertions_help_frame.setGeometry(QRect(0, 0, 208, 911))
        self.verticalLayout_34 = QVBoxLayout(self.scrollArea_convertions_help_frame)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.help_conversions_label = QLabel(self.scrollArea_convertions_help_frame)
        self.help_conversions_label.setObjectName(u"help_conversions_label")
        self.help_conversions_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_conversions_label.setWordWrap(True)
        self.help_conversions_label.setMargin(0)
        self.help_conversions_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_34.addWidget(self.help_conversions_label)

        self.scrollArea_convertions_help.setWidget(self.scrollArea_convertions_help_frame)

        self.verticalLayout_37.addWidget(self.scrollArea_convertions_help)

        self.help_tab_widgets.addTab(self.conversions_help_tab, "")
        self.settings_help_tab = QWidget()
        self.settings_help_tab.setObjectName(u"settings_help_tab")
        self.verticalLayout_38 = QVBoxLayout(self.settings_help_tab)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_settings_help = QScrollArea(self.settings_help_tab)
        self.scrollArea_settings_help.setObjectName(u"scrollArea_settings_help")
        self.scrollArea_settings_help.setWidgetResizable(True)
        self.scrollArea_settings_help_frame = QWidget()
        self.scrollArea_settings_help_frame.setObjectName(u"scrollArea_settings_help_frame")
        self.scrollArea_settings_help_frame.setGeometry(QRect(0, 0, 208, 2181))
        self.verticalLayout_35 = QVBoxLayout(self.scrollArea_settings_help_frame)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.help_settings_label = QLabel(self.scrollArea_settings_help_frame)
        self.help_settings_label.setObjectName(u"help_settings_label")
        self.help_settings_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.help_settings_label.setWordWrap(True)
        self.help_settings_label.setMargin(0)
        self.help_settings_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_35.addWidget(self.help_settings_label)

        self.scrollArea_settings_help.setWidget(self.scrollArea_settings_help_frame)

        self.verticalLayout_38.addWidget(self.scrollArea_settings_help)

        self.help_tab_widgets.addTab(self.settings_help_tab, "")

        self.verticalLayout_8.addWidget(self.help_tab_widgets)


        self.horizontalLayout_8.addWidget(self.help_frame)

        self.content_menu.addWidget(self.Help)

        self.verticalLayout_4.addWidget(self.content_menu)


        self.verticalLayout_2.addWidget(self.options_frame, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_container = QFrame(self.body)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"#top_frame{\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #e8e8e8;\n"
"}")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_btn_frame = QFrame(self.top_frame)
        self.menu_btn_frame.setObjectName(u"menu_btn_frame")
        self.menu_btn_frame.setStyleSheet(u"")
        self.menu_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menu_btn_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.disp_menu_btn = QPushButton(self.menu_btn_frame)
        self.disp_menu_btn.setObjectName(u"disp_menu_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.disp_menu_btn.sizePolicy().hasHeightForWidth())
        self.disp_menu_btn.setSizePolicy(sizePolicy5)
        self.disp_menu_btn.setMinimumSize(QSize(100, 0))
        self.disp_menu_btn.setMaximumSize(QSize(166600, 16777215))
        self.disp_menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disp_menu_btn.setStyleSheet(u"#disp_menu_btn{\n"
"height: 35px;\n"
"margin: 5px;\n"
"background-color: white;\n"
"border-bottom: 1px solid #C2C3C3;\n"
"}\n"
"#disp_menu_btn:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
"#disp_menu_btn:pressed{\n"
"padding-top: 7px;\n"
"padding-left: 5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/sprites/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disp_menu_btn.setIcon(icon)
        self.disp_menu_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.disp_menu_btn, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.menu_btn_frame, 0, Qt.AlignVCenter)

        self.top_buttons = QFrame(self.top_frame)
        self.top_buttons.setObjectName(u"top_buttons")
        self.top_buttons.setStyleSheet(u"#top_buttons{\n"
"margin:5px;\n"
"background-color: white;\n"
"border-radius: 10px;\n"
"border-bottom: 1px solid #C2C3C3;\n"
"}\n"
"QPushButton{\n"
"margin: 5px 2px;\n"
"}")
        self.top_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.top_buttons)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.top_buttons)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/sprites/icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon1)
        self.min_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.min_btn)

        self.restore_size_btn = QPushButton(self.top_buttons)
        self.restore_size_btn.setObjectName(u"restore_size_btn")
        self.restore_size_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restore_size_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/sprites/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_size_btn.setIcon(icon2)
        self.restore_size_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.restore_size_btn)

        self.close_btn = QPushButton(self.top_buttons)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/sprites/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.close_btn)


        self.horizontalLayout_3.addWidget(self.top_buttons, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.top_frame)

        self.results_frame = QFrame(self.main_container)
        self.results_frame.setObjectName(u"results_frame")
        sizePolicy3.setHeightForWidth(self.results_frame.sizePolicy().hasHeightForWidth())
        self.results_frame.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Algeko Personal Use")
        self.results_frame.setFont(font1)
        self.results_frame.setStyleSheet(u"QFrame{\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"margin-top: 10px;\n"
"}\n"
"QFrame QLineEdit{\n"
"font: 8pt \"Algeko Personal Use\";\n"
"color: #4F4F4F;\n"
"selection-background-color: #efefef;\n"
"selection-color: #AFAFAF;\n"
"padding-right: 10px;\n"
"margin-top: 5px;\n"
"margin-right: 5px;\n"
"margin-left: 5px;\n"
"border-radius:5px;\n"
"border-bottom: 1px solid #C2C3C3;\n"
"}\n"
"QFrame #results_line{\n"
"font: 20pt \"Algeko Personal Use\";\n"
"margin-bottom: 5px;\n"
"}")
        self.results_frame.setFrameShape(QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.results_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.second_results_line = QLineEdit(self.results_frame)
        self.second_results_line.setObjectName(u"second_results_line")
        self.second_results_line.setMinimumSize(QSize(0, 35))
        self.second_results_line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.second_results_line.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.second_results_line)

        self.results_line = QLineEdit(self.results_frame)
        self.results_line.setObjectName(u"results_line")
        sizePolicy4.setHeightForWidth(self.results_line.sizePolicy().hasHeightForWidth())
        self.results_line.setSizePolicy(sizePolicy4)
        self.results_line.setMaximumSize(QSize(16777, 16777215))
        font2 = QFont()
        font2.setFamily(u"Algeko Personal Use")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.results_line.setFont(font2)
        self.results_line.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.results_line.setReadOnly(False)
        self.results_line.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.results_line.setClearButtonEnabled(False)

        self.verticalLayout_5.addWidget(self.results_line)


        self.verticalLayout.addWidget(self.results_frame)

        self.footer_main = QFrame(self.main_container)
        self.footer_main.setObjectName(u"footer_main")
        sizePolicy3.setHeightForWidth(self.footer_main.sizePolicy().hasHeightForWidth())
        self.footer_main.setSizePolicy(sizePolicy3)
        self.footer_main.setMinimumSize(QSize(0, 500))
        self.footer_main.setFrameShape(QFrame.StyledPanel)
        self.footer_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_main)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 0)
        self.tabWidget_btns = QTabWidget(self.footer_main)
        self.tabWidget_btns.setObjectName(u"tabWidget_btns")
        self.tabWidget_btns.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget_btns.setStyleSheet(u"QWidget{\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"}\n"
"/* BUTTONS */\n"
"QPushButton{\n"
"height: 30px;\n"
"font: 12px \"Roboto\";\n"
"color:#393939;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"text-align: center;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top: 12px;\n"
"padding-left: 5px;\n"
"}\n"
" /* TABS BOTTOM */\n"
"QTabBar::tab{\n"
"width:100%;\n"
"height: 1.5em;\n"
"font: 10px \"Roboto\";\n"
"padding: 5px;\n"
"text-align: center;\n"
"color:#393939;\n"
"border: none;\n"
"}\n"
"QTabBar::tab:hover{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"QTabBar::tab:selected{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}")
        self.tabWidget_btns.setTabPosition(QTabWidget.South)
        self.tabWidget_btns.setTabShape(QTabWidget.Rounded)
        self.tabWidget_btns.setIconSize(QSize(20, 20))
        self.tabWidget_btns.setElideMode(Qt.ElideRight)
        self.tabWidget_btns.setUsesScrollButtons(False)
        self.tabWidget_btns.setDocumentMode(True)
        self.tabWidget_btns.setTabsClosable(False)
        self.tabWidget_btns.setMovable(True)
        self.standar = QWidget()
        self.standar.setObjectName(u"standar")
        self.standar.setStyleSheet(u"QPushButton{\n"
"height: 60px;\n"
"font: 17px \"Roboto\";\n"
"color:#393939;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"text-align: center;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top: 15px;\n"
"padding-left: 5px;\n"
"}")
        self.gridLayout = QGridLayout(self.standar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.C_btn = QPushButton(self.standar)
        self.C_btn.setObjectName(u"C_btn")
        self.C_btn.setMinimumSize(QSize(0, 70))
        self.C_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.C_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.C_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.C_btn, 0, 0, 1, 1)

        self.one = QPushButton(self.standar)
        self.one.setObjectName(u"one")
        self.one.setMinimumSize(QSize(0, 70))
        self.one.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.one, 4, 0, 1, 1)

        self.multiply_btn = QPushButton(self.standar)
        self.multiply_btn.setObjectName(u"multiply_btn")
        self.multiply_btn.setMinimumSize(QSize(0, 70))
        self.multiply_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.multiply_btn, 0, 3, 1, 1)

        self.minus = QPushButton(self.standar)
        self.minus.setObjectName(u"minus")
        self.minus.setMinimumSize(QSize(0, 70))
        self.minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.minus, 1, 5, 1, 1)

        self.nine = QPushButton(self.standar)
        self.nine.setObjectName(u"nine")
        self.nine.setMinimumSize(QSize(0, 70))
        self.nine.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.nine, 1, 3, 1, 1)

        self.div_btn = QPushButton(self.standar)
        self.div_btn.setObjectName(u"div_btn")
        self.div_btn.setMinimumSize(QSize(0, 70))
        self.div_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.div_btn, 0, 1, 1, 1)

        self.seven = QPushButton(self.standar)
        self.seven.setObjectName(u"seven")
        self.seven.setMinimumSize(QSize(0, 70))
        self.seven.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.seven, 1, 0, 1, 1)

        self.five = QPushButton(self.standar)
        self.five.setObjectName(u"five")
        self.five.setMinimumSize(QSize(0, 70))
        self.five.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.five, 3, 1, 1, 1)

        self.eight = QPushButton(self.standar)
        self.eight.setObjectName(u"eight")
        self.eight.setMinimumSize(QSize(0, 70))
        self.eight.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.eight, 1, 1, 1, 1)

        self.dot_btn = QPushButton(self.standar)
        self.dot_btn.setObjectName(u"dot_btn")
        self.dot_btn.setMinimumSize(QSize(0, 70))
        self.dot_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.dot_btn, 5, 3, 1, 1)

        self.back_btn = QPushButton(self.standar)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMinimumSize(QSize(0, 70))
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.back_btn, 0, 5, 1, 1)

        self.result_btn = QPushButton(self.standar)
        self.result_btn.setObjectName(u"result_btn")
        self.result_btn.setMinimumSize(QSize(0, 170))
        self.result_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.result_btn.setStyleSheet(u"#result_btn{\n"
"background-color: #9fddff;\n"
"color: white;\n"
"font-size: 30px\n"
"}\n"
"#result_btn:hover{\n"
"background-color: #85cbf8\n"
"}\n"
"")

        self.gridLayout.addWidget(self.result_btn, 4, 5, 2, 1)

        self.porcent_btn = QPushButton(self.standar)
        self.porcent_btn.setObjectName(u"porcent_btn")
        self.porcent_btn.setMinimumSize(QSize(0, 70))
        self.porcent_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.porcent_btn, 5, 0, 1, 1)

        self.three = QPushButton(self.standar)
        self.three.setObjectName(u"three")
        self.three.setMinimumSize(QSize(0, 70))
        self.three.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.three, 4, 3, 1, 1)

        self.two = QPushButton(self.standar)
        self.two.setObjectName(u"two")
        self.two.setMinimumSize(QSize(0, 70))
        self.two.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.two, 4, 1, 1, 1)

        self.plus_btn = QPushButton(self.standar)
        self.plus_btn.setObjectName(u"plus_btn")
        self.plus_btn.setMinimumSize(QSize(0, 70))
        self.plus_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.plus_btn, 3, 5, 1, 1)

        self.six = QPushButton(self.standar)
        self.six.setObjectName(u"six")
        self.six.setMinimumSize(QSize(0, 70))
        self.six.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.six, 3, 3, 1, 1)

        self.zero = QPushButton(self.standar)
        self.zero.setObjectName(u"zero")
        self.zero.setMinimumSize(QSize(0, 70))
        self.zero.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.zero, 5, 1, 1, 1)

        self.four = QPushButton(self.standar)
        self.four.setObjectName(u"four")
        self.four.setMinimumSize(QSize(0, 70))
        self.four.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.four, 3, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u":/Icons/sprites/icons/math.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_btns.addTab(self.standar, icon4, "")
        self.C_btn.raise_()
        self.one.raise_()
        self.multiply_btn.raise_()
        self.minus.raise_()
        self.nine.raise_()
        self.div_btn.raise_()
        self.seven.raise_()
        self.five.raise_()
        self.eight.raise_()
        self.dot_btn.raise_()
        self.back_btn.raise_()
        self.result_btn.raise_()
        self.porcent_btn.raise_()
        self.two.raise_()
        self.plus_btn.raise_()
        self.six.raise_()
        self.zero.raise_()
        self.four.raise_()
        self.three.raise_()
        self.science = QWidget()
        self.science.setObjectName(u"science")
        self.gridLayout_2 = QGridLayout(self.science)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.one_2 = QPushButton(self.science)
        self.one_2.setObjectName(u"one_2")
        self.one_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.one_2, 5, 3, 1, 1)

        self.abs = QPushButton(self.science)
        self.abs.setObjectName(u"abs")
        self.abs.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.abs, 1, 4, 1, 1)

        self.npr = QPushButton(self.science)
        self.npr.setObjectName(u"npr")
        self.npr.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.npr, 0, 1, 1, 1)

        self.one_div_x = QPushButton(self.science)
        self.one_div_x.setObjectName(u"one_div_x")
        self.one_div_x.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.one_div_x, 1, 3, 1, 1)

        self.ten_power10 = QPushButton(self.science)
        self.ten_power10.setObjectName(u"ten_power10")
        self.ten_power10.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.ten_power10, 4, 0, 1, 1)

        self.euler = QPushButton(self.science)
        self.euler.setObjectName(u"euler")
        self.euler.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.euler, 0, 4, 1, 1)

        self.closed_bracket = QPushButton(self.science)
        self.closed_bracket.setObjectName(u"closed_bracket")
        self.closed_bracket.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.closed_bracket, 2, 4, 1, 1)

        self.eight_2 = QPushButton(self.science)
        self.eight_2.setObjectName(u"eight_2")
        self.eight_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.eight_2, 3, 4, 1, 1)

        self.multiply = QPushButton(self.science)
        self.multiply.setObjectName(u"multiply")
        self.multiply.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.multiply, 3, 6, 1, 1)

        self.pi = QPushButton(self.science)
        self.pi.setObjectName(u"pi")
        self.pi.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/sprites/icons/pi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pi.setIcon(icon5)
        self.pi.setIconSize(QSize(14, 14))

        self.gridLayout_2.addWidget(self.pi, 0, 3, 1, 1)

        self.logy = QPushButton(self.science)
        self.logy.setObjectName(u"logy")
        self.logy.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.logy, 5, 1, 1, 1)

        self.result = QPushButton(self.science)
        self.result.setObjectName(u"result")
        self.result.setCursor(QCursor(Qt.PointingHandCursor))
        self.result.setStyleSheet(u"#result{\n"
"background-color: #9fddff;\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"#result:hover{\n"
"background-color: #85cbf8\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.result, 6, 6, 1, 1)

        self.x_power2 = QPushButton(self.science)
        self.x_power2.setObjectName(u"x_power2")
        self.x_power2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.x_power2, 1, 0, 1, 1)

        self.cb_root = QPushButton(self.science)
        self.cb_root.setObjectName(u"cb_root")
        self.cb_root.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/sprites/icons/crrt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_root.setIcon(icon6)
        self.cb_root.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.cb_root, 2, 1, 1, 1)

        self.two_2 = QPushButton(self.science)
        self.two_2.setObjectName(u"two_2")
        self.two_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.two_2, 5, 4, 1, 1)

        self.C_btn_2 = QPushButton(self.science)
        self.C_btn_2.setObjectName(u"C_btn_2")
        self.C_btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.C_btn_2, 0, 5, 1, 1)

        self.three_2 = QPushButton(self.science)
        self.three_2.setObjectName(u"three_2")
        self.three_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.three_2, 5, 5, 1, 1)

        self.factorial = QPushButton(self.science)
        self.factorial.setObjectName(u"factorial")
        self.factorial.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.factorial, 2, 5, 1, 1)

        self.ln = QPushButton(self.science)
        self.ln.setObjectName(u"ln")
        self.ln.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.ln, 6, 0, 1, 1)

        self.seven_2 = QPushButton(self.science)
        self.seven_2.setObjectName(u"seven_2")
        self.seven_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.seven_2, 3, 3, 1, 1)

        self.back_btn_2 = QPushButton(self.science)
        self.back_btn_2.setObjectName(u"back_btn_2")
        self.back_btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.back_btn_2, 0, 6, 1, 1)

        self.zero_2 = QPushButton(self.science)
        self.zero_2.setObjectName(u"zero_2")
        self.zero_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.zero_2, 6, 4, 1, 1)

        self.two_powerx = QPushButton(self.science)
        self.two_powerx.setObjectName(u"two_powerx")
        self.two_powerx.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.two_powerx, 4, 1, 1, 1)

        self.four_2 = QPushButton(self.science)
        self.four_2.setObjectName(u"four_2")
        self.four_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.four_2, 4, 3, 1, 1)

        self.log = QPushButton(self.science)
        self.log.setObjectName(u"log")
        self.log.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.log, 5, 0, 1, 1)

        self.plus = QPushButton(self.science)
        self.plus.setObjectName(u"plus")
        self.plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.plus, 5, 6, 1, 1)

        self.minus_2 = QPushButton(self.science)
        self.minus_2.setObjectName(u"minus_2")
        self.minus_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.minus_2, 4, 6, 1, 1)

        self.plus_minus = QPushButton(self.science)
        self.plus_minus.setObjectName(u"plus_minus")
        self.plus_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.plus_minus, 6, 3, 1, 1)

        self.x_power3 = QPushButton(self.science)
        self.x_power3.setObjectName(u"x_power3")
        self.x_power3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.x_power3, 1, 1, 1, 1)

        self.open_bracket = QPushButton(self.science)
        self.open_bracket.setObjectName(u"open_bracket")
        self.open_bracket.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.open_bracket, 2, 3, 1, 1)

        self.ncr = QPushButton(self.science)
        self.ncr.setObjectName(u"ncr")
        self.ncr.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.ncr, 0, 0, 1, 1)

        self.eng_p = QPushButton(self.science)
        self.eng_p.setObjectName(u"eng_p")
        self.eng_p.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.eng_p, 1, 5, 1, 1)

        self.five_2 = QPushButton(self.science)
        self.five_2.setObjectName(u"five_2")
        self.five_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.five_2, 4, 4, 1, 1)

        self.six_2 = QPushButton(self.science)
        self.six_2.setObjectName(u"six_2")
        self.six_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.six_2, 4, 5, 1, 1)

        self.eng_m = QPushButton(self.science)
        self.eng_m.setObjectName(u"eng_m")
        self.eng_m.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.eng_m, 1, 6, 1, 1)

        self.divide_btn = QPushButton(self.science)
        self.divide_btn.setObjectName(u"divide_btn")
        self.divide_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.divide_btn, 2, 6, 1, 1)

        self.dot = QPushButton(self.science)
        self.dot.setObjectName(u"dot")
        self.dot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.dot, 6, 5, 1, 1)

        self.e_powerx = QPushButton(self.science)
        self.e_powerx.setObjectName(u"e_powerx")
        self.e_powerx.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.e_powerx, 6, 1, 1, 1)

        self.nine_2 = QPushButton(self.science)
        self.nine_2.setObjectName(u"nine_2")
        self.nine_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.nine_2, 3, 5, 1, 1)

        self.sq_root = QPushButton(self.science)
        self.sq_root.setObjectName(u"sq_root")
        self.sq_root.setCursor(QCursor(Qt.PointingHandCursor))
        self.sq_root.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/sprites/icons/sqrt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sq_root.setIcon(icon7)
        self.sq_root.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.sq_root, 2, 0, 1, 1)

        self.x_yroot = QPushButton(self.science)
        self.x_yroot.setObjectName(u"x_yroot")
        self.x_yroot.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/sprites/icons/yroot.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.x_yroot.setIcon(icon8)
        self.x_yroot.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.x_yroot, 3, 0, 1, 1)

        self.x_powery = QPushButton(self.science)
        self.x_powery.setObjectName(u"x_powery")
        self.x_powery.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.x_powery, 3, 1, 1, 1)

        icon9 = QIcon()
        icon9.addFile(u":/Icons/sprites/icons/science.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_btns.addTab(self.science, icon9, "")
        self.trigo = QWidget()
        self.trigo.setObjectName(u"trigo")
        self.gridLayout_3 = QGridLayout(self.trigo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.four_3 = QPushButton(self.trigo)
        self.four_3.setObjectName(u"four_3")
        self.four_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.four_3, 5, 0, 1, 1)

        self.csc_btn = QPushButton(self.trigo)
        self.csc_btn.setObjectName(u"csc_btn")
        self.csc_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.csc_btn, 2, 0, 1, 1)

        self.pi_2 = QPushButton(self.trigo)
        self.pi_2.setObjectName(u"pi_2")
        self.pi_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pi_2.setIcon(icon5)
        self.pi_2.setIconSize(QSize(14, 14))

        self.gridLayout_3.addWidget(self.pi_2, 1, 3, 1, 1)

        self.euler_2 = QPushButton(self.trigo)
        self.euler_2.setObjectName(u"euler_2")
        self.euler_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.euler_2, 2, 3, 1, 1)

        self.two_3 = QPushButton(self.trigo)
        self.two_3.setObjectName(u"two_3")
        self.two_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.two_3, 6, 1, 1, 1)

        self.ctg_btn = QPushButton(self.trigo)
        self.ctg_btn.setObjectName(u"ctg_btn")
        self.ctg_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.ctg_btn, 2, 2, 1, 1)

        self.nine_3 = QPushButton(self.trigo)
        self.nine_3.setObjectName(u"nine_3")
        self.nine_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.nine_3, 4, 2, 1, 1)

        self.sin_btn = QPushButton(self.trigo)
        self.sin_btn.setObjectName(u"sin_btn")
        self.sin_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.sin_btn, 1, 0, 1, 1)

        self.one_3 = QPushButton(self.trigo)
        self.one_3.setObjectName(u"one_3")
        self.one_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.one_3, 6, 0, 1, 1)

        self.six_3 = QPushButton(self.trigo)
        self.six_3.setObjectName(u"six_3")
        self.six_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.six_3, 5, 2, 1, 1)

        self.cos_btn = QPushButton(self.trigo)
        self.cos_btn.setObjectName(u"cos_btn")
        self.cos_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.cos_btn, 1, 1, 1, 1)

        self.sec_btn = QPushButton(self.trigo)
        self.sec_btn.setObjectName(u"sec_btn")
        self.sec_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.sec_btn, 2, 1, 1, 1)

        self.dot_3 = QPushButton(self.trigo)
        self.dot_3.setObjectName(u"dot_3")
        self.dot_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.dot_3.setStyleSheet(u"font-size: 18px;")

        self.gridLayout_3.addWidget(self.dot_3, 7, 2, 1, 1)

        self.tan_btn = QPushButton(self.trigo)
        self.tan_btn.setObjectName(u"tan_btn")
        self.tan_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.tan_btn, 1, 2, 1, 1)

        self.five_3 = QPushButton(self.trigo)
        self.five_3.setObjectName(u"five_3")
        self.five_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.five_3, 5, 1, 1, 1)

        self.zero_3 = QPushButton(self.trigo)
        self.zero_3.setObjectName(u"zero_3")
        self.zero_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.zero_3, 7, 1, 1, 1)

        self.eight_3 = QPushButton(self.trigo)
        self.eight_3.setObjectName(u"eight_3")
        self.eight_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.eight_3, 4, 1, 1, 1)

        self.seven_3 = QPushButton(self.trigo)
        self.seven_3.setObjectName(u"seven_3")
        self.seven_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.seven_3, 4, 0, 1, 1)

        self.three_3 = QPushButton(self.trigo)
        self.three_3.setObjectName(u"three_3")
        self.three_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.three_3, 6, 2, 1, 1)

        self.back_btn_3 = QPushButton(self.trigo)
        self.back_btn_3.setObjectName(u"back_btn_3")
        self.back_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn_3.setStyleSheet(u"font-size: 14px;")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/sprites/icons/hand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn_3.setIcon(icon10)

        self.gridLayout_3.addWidget(self.back_btn_3, 0, 2, 1, 2)

        self.C_btn_3 = QPushButton(self.trigo)
        self.C_btn_3.setObjectName(u"C_btn_3")
        self.C_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.C_btn_3.setStyleSheet(u"font-size: 14px;")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/sprites/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.C_btn_3.setIcon(icon11)
        self.C_btn_3.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.C_btn_3, 0, 0, 1, 2)

        self.arcsin = QPushButton(self.trigo)
        self.arcsin.setObjectName(u"arcsin")
        self.arcsin.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.arcsin, 3, 0, 1, 1)

        self.arcos = QPushButton(self.trigo)
        self.arcos.setObjectName(u"arcos")
        self.arcos.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.arcos, 3, 1, 1, 1)

        self.arctan = QPushButton(self.trigo)
        self.arctan.setObjectName(u"arctan")
        self.arctan.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.arctan, 3, 2, 1, 1)

        self.multiply_btn_3 = QPushButton(self.trigo)
        self.multiply_btn_3.setObjectName(u"multiply_btn_3")
        self.multiply_btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.multiply_btn_3, 5, 3, 1, 1)

        self.div_btn_3 = QPushButton(self.trigo)
        self.div_btn_3.setObjectName(u"div_btn_3")
        self.div_btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.div_btn_3, 7, 0, 1, 1)

        self.minus_btn2 = QPushButton(self.trigo)
        self.minus_btn2.setObjectName(u"minus_btn2")
        self.minus_btn2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.minus_btn2, 3, 3, 1, 1)

        self.plus_btn_2 = QPushButton(self.trigo)
        self.plus_btn_2.setObjectName(u"plus_btn_2")
        self.plus_btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.plus_btn_2, 4, 3, 1, 1)

        self.result_3 = QPushButton(self.trigo)
        self.result_3.setObjectName(u"result_3")
        self.result_3.setMinimumSize(QSize(0, 110))
        self.result_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.result_3.setStyleSheet(u"#result_3{\n"
"background-color: #9fddff;\n"
"color: white;\n"
"font-size: 18px;\n"
"}\n"
"#result_3:hover{\n"
"background-color: #85cbf8\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.result_3, 6, 3, 2, 1)

        icon12 = QIcon()
        icon12.addFile(u":/Icons/sprites/icons/trigonometry.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget_btns.addTab(self.trigo, icon12, "")

        self.horizontalLayout_6.addWidget(self.tabWidget_btns)

        self.manual_tab = QTabWidget(self.footer_main)
        self.manual_tab.setObjectName(u"manual_tab")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.manual_tab.sizePolicy().hasHeightForWidth())
        self.manual_tab.setSizePolicy(sizePolicy6)
        self.manual_tab.setMaximumSize(QSize(500, 16777215))
        self.manual_tab.setCursor(QCursor(Qt.ArrowCursor))
        self.manual_tab.setStyleSheet(u"QWidget{\n"
"background-color: #efefef;\n"
"border-radius: 10px;\n"
"} \n"
"/* QLabel */\n"
"QLabel{\n"
"background-color: white;\n"
"font: 14px \"Roboto\";\n"
"color:#393939;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"selection-background-color: #efefef;\n"
"selection-color: #AFAFAF;\n"
"}\n"
"/* BUTTONS */\n"
"QPushButton{\n"
"height: 30px;\n"
"font: 11px \"Roboto\";\n"
"color:#393939;\n"
"background-color: #ffffff;\n"
"border-radius: 5px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;\n"
"text-align: center;\n"
"widget-animation-duration: 100;\n"
"border-bottom: 1px solid #C6C6C6;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #E0E0E0;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top: 12px;\n"
"padding-left: 5px;\n"
"}\n"
"/* QLineEdit */\n"
"QFrame QLineEdit{\n"
"height: 20px;\n"
"background-color: white;\n"
"font: 12px \"Roboto\";\n"
"color: #383939;\n"
"selection-background-color: #efefef;\n"
"selection-color: #AFAFAF;\n"
"padding: 5px;\n"
"margin-right: 10px;\n"
"margin-left: "
                        "10px;\n"
"border-radius:3px;\n"
"border-bottom: 1px solid #C2C3C3;\n"
"}\n"
" /* TABS BOTTOM */\n"
"QTabBar::tab{\n"
"width:115px;\n"
"height: 1.5em;\n"
"font: 10px \"Roboto\";\n"
"padding: 5px;\n"
"text-align: center;\n"
"color:#393939;\n"
"border: none;\n"
"}\n"
"QTabBar::tab:hover{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"QTabBar::tab:selected{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"}\n"
"/* QComboBox */\n"
"QComboBox{\n"
"background-color: white;\n"
"color: #393939;\n"
"height: 50px;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"margin: 10px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"font: 12px \"Roboto\";\n"
"}\n"
"QComboBox::drop-down{\n"
"background: #E5E5E5;\n"
"color: #AFAFAF;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"QComboBox::drop-down:hover{\n"
"background: #C3C2C2;\n"
"color: white;\n"
"}\n"
"QComboBox::drop-down:on{\n"
"background: #AFAFAF;\n"
"}\n"
"/* POPUP ELEMENTS */\n"
"QComboBox QAbstractItemView {\n"
"background: white;\n"
""
                        "selection-background-color: #E5E5E5;\n"
"selection-color: #393939;\n"
"border: none;\n"
"outline: none;\n"
"font: 12px \"Roboto\";\n"
"color: #393939;\n"
"}\n"
"QScrollBar:vertical {\n"
"background: white;\n"
"width: 1em;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"background:rgb(195, 194, 194);\n"
"border-radius: 3px;\n"
"width: 0px;\n"
"position: absolute;\n"
"}\n"
"")
        self.manual_tab.setTabPosition(QTabWidget.South)
        self.manual_tab.setTabShape(QTabWidget.Rounded)
        self.manual_tab.setIconSize(QSize(20, 20))
        self.manual_tab.setUsesScrollButtons(False)
        self.manual_tab.setMovable(True)
        self.manual_tab.setTabBarAutoHide(False)
        self.historial_frame = QWidget()
        self.historial_frame.setObjectName(u"historial_frame")
        self.verticalLayout_14 = QVBoxLayout(self.historial_frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.historial_frame_label = QFrame(self.historial_frame)
        self.historial_frame_label.setObjectName(u"historial_frame_label")
        sizePolicy3.setHeightForWidth(self.historial_frame_label.sizePolicy().hasHeightForWidth())
        self.historial_frame_label.setSizePolicy(sizePolicy3)
        self.historial_frame_label.setFrameShape(QFrame.Panel)
        self.historial_frame_label.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.historial_frame_label)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_hist = QScrollArea(self.historial_frame_label)
        self.scrollArea_hist.setObjectName(u"scrollArea_hist")
        self.scrollArea_hist.setWidgetResizable(True)
        self.historial_content_scroll = QWidget()
        self.historial_content_scroll.setObjectName(u"historial_content_scroll")
        self.historial_content_scroll.setGeometry(QRect(0, 0, 498, 406))
        self.verticalLayout_17 = QVBoxLayout(self.historial_content_scroll)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.historial_label = QLabel(self.historial_content_scroll)
        self.historial_label.setObjectName(u"historial_label")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.historial_label.setFont(font3)
        self.historial_label.setCursor(QCursor(Qt.ArrowCursor))
        self.historial_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.historial_label.setMargin(30)
        self.historial_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_17.addWidget(self.historial_label)

        self.scrollArea_hist.setWidget(self.historial_content_scroll)

        self.verticalLayout_15.addWidget(self.scrollArea_hist)


        self.verticalLayout_14.addWidget(self.historial_frame_label)

        self.historial_frame_btns = QFrame(self.historial_frame)
        self.historial_frame_btns.setObjectName(u"historial_frame_btns")
        self.historial_frame_btns.setMinimumSize(QSize(0, 30))
        self.historial_frame_btns.setFrameShape(QFrame.StyledPanel)
        self.historial_frame_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.historial_frame_btns)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 2)
        self.reset_historial_btn = QPushButton(self.historial_frame_btns)
        self.reset_historial_btn.setObjectName(u"reset_historial_btn")
        self.reset_historial_btn.setMinimumSize(QSize(100, 0))
        self.reset_historial_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_historial_btn.setStyleSheet(u"margin: 5px;\n"
"width: 350px")
        self.reset_historial_btn.setIcon(icon11)
        self.reset_historial_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.reset_historial_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.historial_frame_btns, 0, Qt.AlignBottom)

        icon13 = QIcon()
        icon13.addFile(u":/Icons/sprites/icons/historial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_tab.addTab(self.historial_frame, icon13, "")
        self.manual_frame = QWidget()
        self.manual_frame.setObjectName(u"manual_frame")
        self.gridLayout_4 = QGridLayout(self.manual_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 5)
        self.up_frame_manual = QFrame(self.manual_frame)
        self.up_frame_manual.setObjectName(u"up_frame_manual")
        self.up_frame_manual.setMaximumSize(QSize(16777215, 150))
        self.up_frame_manual.setFrameShape(QFrame.StyledPanel)
        self.up_frame_manual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.up_frame_manual)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.select_operation_title = QLabel(self.up_frame_manual)
        self.select_operation_title.setObjectName(u"select_operation_title")
        self.select_operation_title.setMaximumSize(QSize(16777215, 50))
        self.select_operation_title.setStyleSheet(u"QLabel{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 14px \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 7px;\n"
"margin-top: 0.7em;\n"
"margin-bottom: 3px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: #393939;\n"
"}")
        self.select_operation_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.select_operation_title)

        self.select_operation_comboBox = QComboBox(self.up_frame_manual)
        self.select_operation_comboBox.addItem("")
        self.select_operation_comboBox.addItem("")
        self.select_operation_comboBox.addItem("")
        self.select_operation_comboBox.addItem("")
        self.select_operation_comboBox.setObjectName(u"select_operation_comboBox")
        self.select_operation_comboBox.setFrame(True)

        self.verticalLayout_18.addWidget(self.select_operation_comboBox)

        self.insert_expression_manual_frame = QFrame(self.up_frame_manual)
        self.insert_expression_manual_frame.setObjectName(u"insert_expression_manual_frame")
        self.insert_expression_manual_frame.setFrameShape(QFrame.StyledPanel)
        self.insert_expression_manual_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.insert_expression_manual_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.insert_exp_title = QLabel(self.insert_expression_manual_frame)
        self.insert_exp_title.setObjectName(u"insert_exp_title")
        self.insert_exp_title.setStyleSheet(u"font-size: 13px;\n"
"margin-left: 10px;\n"
"border-radius: 3px;\n"
"padding: 3px;")

        self.horizontalLayout_10.addWidget(self.insert_exp_title)

        self.expression_lineEdit = QLineEdit(self.insert_expression_manual_frame)
        self.expression_lineEdit.setObjectName(u"expression_lineEdit")

        self.horizontalLayout_10.addWidget(self.expression_lineEdit)


        self.verticalLayout_18.addWidget(self.insert_expression_manual_frame)

        self.get_draw_manual_btn = QPushButton(self.up_frame_manual)
        self.get_draw_manual_btn.setObjectName(u"get_draw_manual_btn")
        self.get_draw_manual_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_draw_manual_btn.setStyleSheet(u"margin: 10px;\n"
"margin-bottom: 0")

        self.verticalLayout_18.addWidget(self.get_draw_manual_btn)


        self.gridLayout_4.addWidget(self.up_frame_manual, 0, 0, 1, 2)

        self.down_frame_manual = QFrame(self.manual_frame)
        self.down_frame_manual.setObjectName(u"down_frame_manual")
        self.down_frame_manual.setFrameShape(QFrame.StyledPanel)
        self.down_frame_manual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.down_frame_manual)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_manual = QScrollArea(self.down_frame_manual)
        self.scroll_area_manual.setObjectName(u"scroll_area_manual")
        self.scroll_area_manual.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_manual.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_manual.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName(u"scroll_content")
        self.scroll_content.setGeometry(QRect(0, 0, 498, 253))
        self.verticalLayout_20 = QVBoxLayout(self.scroll_content)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.drawing_frame = QLabel(self.scroll_content)
        self.drawing_frame.setObjectName(u"drawing_frame")
        self.drawing_frame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.drawing_frame.setMargin(30)

        self.verticalLayout_20.addWidget(self.drawing_frame)

        self.scroll_area_manual.setWidget(self.scroll_content)

        self.verticalLayout_19.addWidget(self.scroll_area_manual)

        self.clear_manual_frame = QPushButton(self.down_frame_manual)
        self.clear_manual_frame.setObjectName(u"clear_manual_frame")
        self.clear_manual_frame.setMaximumSize(QSize(350, 16777215))
        self.clear_manual_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.clear_manual_frame.setStyleSheet(u"margin: 5px;\n"
"width: 350px")
        self.clear_manual_frame.setIcon(icon11)
        self.clear_manual_frame.setIconSize(QSize(25, 25))

        self.verticalLayout_19.addWidget(self.clear_manual_frame, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.down_frame_manual, 1, 0, 1, 2)

        icon14 = QIcon()
        icon14.addFile(u":/Icons/sprites/icons/paint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_tab.addTab(self.manual_frame, icon14, "")
        self.conversions_tab = QWidget()
        self.conversions_tab.setObjectName(u"conversions_tab")
        self.verticalLayout_21 = QVBoxLayout(self.conversions_tab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.convertions_head_frame = QFrame(self.conversions_tab)
        self.convertions_head_frame.setObjectName(u"convertions_head_frame")
        sizePolicy3.setHeightForWidth(self.convertions_head_frame.sizePolicy().hasHeightForWidth())
        self.convertions_head_frame.setSizePolicy(sizePolicy3)
        self.convertions_head_frame.setMinimumSize(QSize(0, 100))
        self.convertions_head_frame.setStyleSheet(u"QFrame {\n"
"background-color: #e8e8e8;\n"
"height: 50px;\n"
"border-radius: 10px;\n"
"}")
        self.convertions_head_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_head_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.convertions_head_frame)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.convertions_head_label = QLabel(self.convertions_head_frame)
        self.convertions_head_label.setObjectName(u"convertions_head_label")
        self.convertions_head_label.setStyleSheet(u"QLabel{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 14px \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 7px;\n"
"margin-top: 5px;\n"
"margin-bottom: 3px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: #393939;\n"
"}")
        self.convertions_head_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.convertions_head_label)

        self.convertions_measure_comboBox = QComboBox(self.convertions_head_frame)
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.addItem("")
        self.convertions_measure_comboBox.setObjectName(u"convertions_measure_comboBox")
        self.convertions_measure_comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.convertions_measure_comboBox.setStyleSheet(u"/* QComboBox */\n"
"QComboBox{\n"
"background-color: white;\n"
"color: #393939;\n"
"height: 50px;\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"margin: 10px;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"font: 12px \"Roboto\";\n"
"}\n"
"QComboBox::drop-down{\n"
"background: #E5E5E5;\n"
"color: #AFAFAF;\n"
"border-top-right-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"}\n"
"QComboBox::drop-down:hover{\n"
"background: #C3C2C2;\n"
"color: white;\n"
"}\n"
"QComboBox::drop-down:on{\n"
"background: #AFAFAF;\n"
"}\n"
"/* POPUP ELEMENTS */\n"
"QComboBox QAbstractItemView {\n"
"background: white;\n"
"selection-background-color: #E5E5E5;\n"
"selection-color: #393939;\n"
"border: none;\n"
"outline: none;\n"
"font: 12px \"Roboto\";\n"
"color: #393939;\n"
"}\n"
"")

        self.verticalLayout_22.addWidget(self.convertions_measure_comboBox)


        self.verticalLayout_21.addWidget(self.convertions_head_frame, 0, Qt.AlignTop)

        self.convertions_body_frame = QFrame(self.conversions_tab)
        self.convertions_body_frame.setObjectName(u"convertions_body_frame")
        sizePolicy3.setHeightForWidth(self.convertions_body_frame.sizePolicy().hasHeightForWidth())
        self.convertions_body_frame.setSizePolicy(sizePolicy3)
        self.convertions_body_frame.setStyleSheet(u"QLabel{\n"
"font-size: 12px;\n"
"padding: 5px;\n"
"}")
        self.convertions_body_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.convertions_body_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.convertions_body_left_frame = QFrame(self.convertions_body_frame)
        self.convertions_body_left_frame.setObjectName(u"convertions_body_left_frame")
        self.convertions_body_left_frame.setMaximumSize(QSize(250, 16777215))
        self.convertions_body_left_frame.setStyleSheet(u"")
        self.convertions_body_left_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.convertions_body_left_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.convertions_body_top_frame = QFrame(self.convertions_body_left_frame)
        self.convertions_body_top_frame.setObjectName(u"convertions_body_top_frame")
        self.convertions_body_top_frame.setStyleSheet(u"#convertions_body_top_frame{\n"
"background-color: #e8e8e8;\n"
"}")
        self.convertions_body_top_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.convertions_body_top_frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.convertions_body_top_label1 = QLabel(self.convertions_body_top_frame)
        self.convertions_body_top_label1.setObjectName(u"convertions_body_top_label1")
        self.convertions_body_top_label1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.convertions_body_top_label1)

        self.convertions_body_top_lineEdit = QLineEdit(self.convertions_body_top_frame)
        self.convertions_body_top_lineEdit.setObjectName(u"convertions_body_top_lineEdit")
        self.convertions_body_top_lineEdit.setMinimumSize(QSize(0, 75))
        self.convertions_body_top_lineEdit.setMaximumSize(QSize(1677, 200))
        self.convertions_body_top_lineEdit.setStyleSheet(u"font-size: 13pt;")
        self.convertions_body_top_lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.convertions_body_top_lineEdit)

        self.convertions_body_top_combo = QComboBox(self.convertions_body_top_frame)
        self.convertions_body_top_combo.setObjectName(u"convertions_body_top_combo")
        self.convertions_body_top_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_24.addWidget(self.convertions_body_top_combo)


        self.verticalLayout_23.addWidget(self.convertions_body_top_frame)

        self.convertions_body_down_frame = QFrame(self.convertions_body_left_frame)
        self.convertions_body_down_frame.setObjectName(u"convertions_body_down_frame")
        self.convertions_body_down_frame.setStyleSheet(u"#convertions_body_down_frame{\n"
"background-color: #e8e8e8;\n"
"}")
        self.convertions_body_down_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_down_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.convertions_body_down_frame)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.convertions_body_down_label1 = QLabel(self.convertions_body_down_frame)
        self.convertions_body_down_label1.setObjectName(u"convertions_body_down_label1")
        self.convertions_body_down_label1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.convertions_body_down_label1)

        self.convertions_body_down_label2 = QLabel(self.convertions_body_down_frame)
        self.convertions_body_down_label2.setObjectName(u"convertions_body_down_label2")
        self.convertions_body_down_label2.setStyleSheet(u"font-size: 13pt;\n"
"padding: 15px;")
        self.convertions_body_down_label2.setAlignment(Qt.AlignCenter)
        self.convertions_body_down_label2.setMargin(30)

        self.verticalLayout_25.addWidget(self.convertions_body_down_label2)

        self.convertions_body_down_combo = QComboBox(self.convertions_body_down_frame)
        self.convertions_body_down_combo.setObjectName(u"convertions_body_down_combo")
        self.convertions_body_down_combo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.convertions_body_down_combo)


        self.verticalLayout_23.addWidget(self.convertions_body_down_frame)


        self.horizontalLayout_11.addWidget(self.convertions_body_left_frame)

        self.convertions_body_right_frame = QFrame(self.convertions_body_frame)
        self.convertions_body_right_frame.setObjectName(u"convertions_body_right_frame")
        self.convertions_body_right_frame.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.convertions_body_right_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.convertions_body_right_frame_top = QFrame(self.convertions_body_right_frame)
        self.convertions_body_right_frame_top.setObjectName(u"convertions_body_right_frame_top")
        self.convertions_body_right_frame_top.setStyleSheet(u"QFrame{\n"
"background-color: #e8e8e8;\n"
"border-radius: 10px;\n"
"}")
        self.convertions_body_right_frame_top.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_right_frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.convertions_body_right_frame_top)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.convertions_body_right_frame_top_title = QLabel(self.convertions_body_right_frame_top)
        self.convertions_body_right_frame_top_title.setObjectName(u"convertions_body_right_frame_top_title")
        self.convertions_body_right_frame_top_title.setMinimumSize(QSize(30, 50))
        self.convertions_body_right_frame_top_title.setStyleSheet(u"QLabel{\n"
"background-color: #C3C2C2;\n"
"color: white;\n"
"border-bottom: 1px solid #AFAFAF;\n"
"border-radius: 5px;\n"
"padding-bottom: 5px;\n"
"font: 14px \"Roboto\";\n"
"text-align: center;\n"
"padding-top: 7px;\n"
"margin-top: 5px;\n"
"margin-bottom: 3px;\n"
"margin-right: 30px;\n"
"margin-left: 30px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: #393939;\n"
"}")
        self.convertions_body_right_frame_top_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.convertions_body_right_frame_top_title)


        self.verticalLayout_26.addWidget(self.convertions_body_right_frame_top, 0, Qt.AlignTop)

        self.convertions_body_right_frame_down = QFrame(self.convertions_body_right_frame)
        self.convertions_body_right_frame_down.setObjectName(u"convertions_body_right_frame_down")
        sizePolicy3.setHeightForWidth(self.convertions_body_right_frame_down.sizePolicy().hasHeightForWidth())
        self.convertions_body_right_frame_down.setSizePolicy(sizePolicy3)
        self.convertions_body_right_frame_down.setFrameShape(QFrame.StyledPanel)
        self.convertions_body_right_frame_down.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.convertions_body_right_frame_down)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.convertions_body_right_frame_down_label1 = QLabel(self.convertions_body_right_frame_down)
        self.convertions_body_right_frame_down_label1.setObjectName(u"convertions_body_right_frame_down_label1")
        self.convertions_body_right_frame_down_label1.setMinimumSize(QSize(0, 30))

        self.verticalLayout_28.addWidget(self.convertions_body_right_frame_down_label1, 0, Qt.AlignTop)

        self.convertions_body_right_frame_down_label2 = QLabel(self.convertions_body_right_frame_down)
        self.convertions_body_right_frame_down_label2.setObjectName(u"convertions_body_right_frame_down_label2")
        sizePolicy4.setHeightForWidth(self.convertions_body_right_frame_down_label2.sizePolicy().hasHeightForWidth())
        self.convertions_body_right_frame_down_label2.setSizePolicy(sizePolicy4)
        self.convertions_body_right_frame_down_label2.setMaximumSize(QSize(250, 16777215))
        self.convertions_body_right_frame_down_label2.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.convertions_body_right_frame_down_label2.setWordWrap(True)
        self.convertions_body_right_frame_down_label2.setMargin(5)

        self.verticalLayout_28.addWidget(self.convertions_body_right_frame_down_label2)


        self.verticalLayout_26.addWidget(self.convertions_body_right_frame_down)


        self.horizontalLayout_11.addWidget(self.convertions_body_right_frame)


        self.verticalLayout_21.addWidget(self.convertions_body_frame)

        icon15 = QIcon()
        icon15.addFile(u":/Icons/sprites/icons/rule.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_tab.addTab(self.conversions_tab, icon15, "")
        self.graphics_frame = QWidget()
        self.graphics_frame.setObjectName(u"graphics_frame")
        self.horizontalLayout_12 = QHBoxLayout(self.graphics_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.coming_soon = QLabel(self.graphics_frame)
        self.coming_soon.setObjectName(u"coming_soon")
        sizePolicy4.setHeightForWidth(self.coming_soon.sizePolicy().hasHeightForWidth())
        self.coming_soon.setSizePolicy(sizePolicy4)
        self.coming_soon.setMinimumSize(QSize(400, 0))
        self.coming_soon.setStyleSheet(u"")
        self.coming_soon.setAlignment(Qt.AlignCenter)
        self.coming_soon.setMargin(5)

        self.horizontalLayout_12.addWidget(self.coming_soon, 0, Qt.AlignHCenter)

        icon16 = QIcon()
        icon16.addFile(u":/Icons/sprites/icons/graphics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_tab.addTab(self.graphics_frame, icon16, "")

        self.horizontalLayout_6.addWidget(self.manual_tab)


        self.verticalLayout.addWidget(self.footer_main)


        self.horizontalLayout.addWidget(self.main_container)


        self.horizontalLayout_2.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.content_menu.setCurrentIndex(2)
        self.settings_tab.setCurrentIndex(3)
        self.help_tab_widgets.setCurrentIndex(0)
        self.tabWidget_btns.setCurrentIndex(2)
        self.manual_tab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"SHANGOO", None))
#if QT_CONFIG(tooltip)
        self.setting_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.setting_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.setting_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.setting_button.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.setting_button.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.setting_button.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.media_button.setText(QCoreApplication.translate("MainWindow", u"  Social Media", None))
#if QT_CONFIG(tooltip)
        self.about_us_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Abouts us</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.about_us_button.setText(QCoreApplication.translate("MainWindow", u"   About us", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply changes", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.language), QCoreApplication.translate("MainWindow", u"Language", None))
        self.angle_title.setText(QCoreApplication.translate("MainWindow", u"Angle measurement units", None))
        self.angle_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"DEG", None))
        self.angle_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CEN", None))
        self.angle_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"RAD", None))

        self.angle_comboBox.setPlaceholderText("")
        self.apply_angle.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.units), QCoreApplication.translate("MainWindow", u"Units", None))
        self.macro_title.setText(QCoreApplication.translate("MainWindow", u"Adjust macros", None))
        ___qtablewidgetitem = self.macros_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Key", None));
        ___qtablewidgetitem1 = self.macros_table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Macro 1", None));
        ___qtablewidgetitem2 = self.macros_table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Macro 2", None));
        ___qtablewidgetitem3 = self.macros_table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Macro 3", None));
        ___qtablewidgetitem4 = self.macros_table_widget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Macro 4", None));
        ___qtablewidgetitem5 = self.macros_table_widget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Macro 5", None));

        __sortingEnabled = self.macros_table_widget.isSortingEnabled()
        self.macros_table_widget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.macros_table_widget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"None", None));
        ___qtablewidgetitem7 = self.macros_table_widget.item(1, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"None", None));
        ___qtablewidgetitem8 = self.macros_table_widget.item(2, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"None", None));
        ___qtablewidgetitem9 = self.macros_table_widget.item(3, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"None", None));
        ___qtablewidgetitem10 = self.macros_table_widget.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"None", None));
        self.macros_table_widget.setSortingEnabled(__sortingEnabled)

        self.save_macros_btn.setText(QCoreApplication.translate("MainWindow", u"Save macros", None))
        self.reset_macros_btn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.use_macro_selected.setText(QCoreApplication.translate("MainWindow", u"Use macro selected", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.macros), QCoreApplication.translate("MainWindow", u"Macros", None))
        self.preferences_title.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.logy_checkbox.setText(QCoreApplication.translate("MainWindow", u"Show \"log y\u207f\" warning", None))
        self.loadscreen_checkbox.setText(QCoreApplication.translate("MainWindow", u"Start with LoadScreen", None))
        self.menu_checkbox.setText(QCoreApplication.translate("MainWindow", u"Start with menu", None))
        self.preferences_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.settings_tab.setTabText(self.settings_tab.indexOf(self.preferences_tab), QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.social_title.setText(QCoreApplication.translate("MainWindow", u"Social Media", None))
        self.facebook_btn.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.youtube_btn.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.instagram_btn.setText(QCoreApplication.translate("MainWindow", u"Instagram", None))
        self.webpage_btn.setText(QCoreApplication.translate("MainWindow", u"Pagina web", None))
        self.help_title.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.help_useful_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Lo m\u00e1s \u00fatil</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">\u00bfQu\u00e9 es Shangoo?</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Shangoo es una calculadora con todas las funciones conocidas, sin embargo, Shangoo incluye funciones \u00fatiles para usuarios ocasionales, las funciones son las siguientes:</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Calculadora est\u00e1ndar</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Calculadora cient\u00edfica</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Calculadora de Trygonometr\u00eda</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Funci\u00f3n hist\u00f3rica</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Operaciones de pintura</span></p>"
                        "<p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Conversiones de medidas</span></p><p align=\"justify\"><span style=\" font-size:9pt; font-style:italic;\">- Gr\u00e1ficos</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo configurar el idioma?</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Configurar o establecer el idioma es tan simple como abrir el men\u00fa lateral presionando el bot\u00f3n de men\u00fa.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">1. Ir a ayudar</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">2. Presione el bot\u00f3n &quot;Configuraci\u00f3n&quot;.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">3. Vaya a la pesta\u00f1a &quot;idioma&quot;.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">4. Seleccione el necesario.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">5. Aplicar los cambios.</span></p><p align=\"justify\"><span styl"
                        "e=\" font-size:9pt;\">Adem\u00e1s, puede agregar cualquier idioma que desee insertando un archivo </span><span style=\" font-size:9pt; font-weight:600;\">json</span><span style=\" font-size:9pt;\"> en el archivo &quot;languages&quot;. Por defecto, Shangoo tiene idioma ingl\u00e9s y espa\u00f1ol, por cierto, el archivo </span><span style=\" font-size:9pt; font-weight:600;\">json</span><span style=\" font-size:9pt;\"> debe contener las mismas claves que los originales.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo comunico una queja?</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">Si desea presentar una queja, vaya al sitio web e ingrese en la secci\u00f3n de preguntas frecuentes. Luego siga los pasos dados en la p\u00e1gina web.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo informo de un error?</span></p><p><span style=\" font-size:9pt;\">Para reportar un bug de Shangoo, entra por tu mail, luego "
                        "escribe un mail con la informaci\u00f3n que consideres necesaria, tambi\u00e9n como sugerencia dejar im\u00e1genes o videos es una buena ayuda para resolver y solucionar tus problemas. Para obtener m\u00e1s informaci\u00f3n, visite la p\u00e1gina web de Shangoo.</span></p></body></html>", None))
        self.help_tab_widgets.setTabText(self.help_tab_widgets.indexOf(self.useful_help_tab), QCoreApplication.translate("MainWindow", u"Useful", None))
        self.help_calculator_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">C\u00f3mo usar las calculadoras Shangoo</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Calculadora est\u00e1ndar</span></p><p><span style=\" font-size:9pt;\">La calculadora est\u00e1ndar es una instancia muy simple de una calculadora, es \u00fatil para usuarios ocasionales, para hacer c\u00e1lculos, adem\u00e1s los ni\u00f1os no tendr\u00e1n complicaciones con su funcionamiento.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Calculadora de ciencia</span></p><p><span style=\" font-size:9pt;\">Usar la calculadora Sciencie es tan f\u00e1cil como usar Standar, sin embargo, hay algunos detalles que probablemente necesite saber para obtener algunos resultados correctamente.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">- Conocimiento previo</span></p><p><span style=\" font-size:9pt; font-style:italic;\">Para usar cualquier calculadora cient\u00ed"
                        "fica, debe comprender las matem\u00e1ticas y, una vez que lo haya hecho, podr\u00e1 ejecutar cualquier funci\u00f3n en las calculadoras cient\u00edficas y de trigonometr\u00eda. Sin embargo, aqu\u00ed est\u00e1n las cosas m\u00e1s interesantes que podr\u00edas necesitar.</span></p><p><br/></p><p><span style=\" text-decoration: underline;\">- nCr</span></p><p>La f\u00f3rmula de combinaci\u00f3n es un m\u00e9todo r\u00e1pido para obtener resultados eficientes sobre la cantidad de combinaciones sin importar el orden. Para usar estas funciones correctamente, primero debe pasar el valor &quot;n&quot; (n\u00famero de combinaciones), luego presionar el bot\u00f3n &quot;nCr&quot; y pasar &quot;r&quot; (cantidad de espacios disponibles para ordenar).</p><p><br/></p><p><span style=\" text-decoration: underline;\">- nPr</span></p><p>La f\u00f3rmula de permutaci\u00f3n es bastante similar a la f\u00f3rmula de combinaci\u00f3n, con la excepci\u00f3n de que, en este caso, el orden s\u00ed importa. El procedimiento para util"
                        "izar correctamente este m\u00e9todo se nombra en las funciones &quot;nCr&quot; por encima de esta definici\u00f3n.</p><p><br/></p><p><span style=\" text-decoration: underline;\">- Valor absoluto</span></p><p>El valor absoluto es una funci\u00f3n matem\u00e1tica definida como la ra\u00edz cuadrada de una x al cuadrado. Esto siempre devuelve un valor positivo, tambi\u00e9n podr\u00eda definirse como la distancia entre el origen en la recta num\u00e9rica.</p><p>Para usarlo, debe presionar el bot\u00f3n, pasar el n\u00famero que necesita y presionar el bot\u00f3n una vez m\u00e1s.</p><p><br/></p><p><span style=\" text-decoration: underline;\">- ENG</span></p><p>La funci\u00f3n de ingeniero es una operaci\u00f3n muy \u00fatil que le permite saber c\u00f3mo es igual a una expresi\u00f3n en notaci\u00f3n cient\u00edfica, al presionar + o - modo ENG, su expresi\u00f3n matem\u00e1tica cambiar\u00e1 a una nueva expresi\u00f3n relativa expresada en notaci\u00f3n cient\u00edfica.</p><p><br/></p><p><span style=\" text-deco"
                        "ration: underline;\">- Factorial (n!)</span></p><p>Un factorial num\u00e9rico se define como ese n\u00famero multiplicado por ese n\u00famero-1 y haciendo lo mismo hasta el n\u00famero uno. Simplemente coloque el n\u00famero que necesita y presione &quot;n!&quot; , obtenga el resultado y vea. Advertencia, los n\u00fameros m\u00e1s altos pueden generar errores u obtener n\u00fameros supergrandes.</p><p><br/></p><p><span style=\" text-decoration: underline;\">- Ra\u00edces</span></p><p>Para obtener una ra\u00edz cuadrada, solo necesita presionar su bot\u00f3n y colocar el n\u00famero, \u00a1y listo! lo hiciste. Sin embargo, para obtener una ra\u00edz Y, deber\u00e1 colocar el n\u00famero Y en el lado izquierdo del s\u00edmbolo &quot;Ra\u00edz&quot;; de lo contrario, obtendr\u00e1 una ra\u00edz cuadrada.</p><p><br/></p><p><span style=\" text-decoration: underline;\">- Logaritmos</span></p><p>El proceso para obtener un logaritmo natural o Log es bastante simple, simplemente coloque el n\u00famero en el lado derech"
                        "o de la funci\u00f3n. En caso de obtener un LOGY, debe poner &quot;^&quot; al lado de su n\u00famero de potencia.</p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Calculadora de trigonometr\u00eda</span></p><p><span style=\" font-size:9pt;\">La calculadora de trigonometr\u00eda de Shangoo es bastante simple, hay todas las funciones trigonom\u00e9tricas que necesita en los conceptos b\u00e1sicos de trigonometr\u00eda.</span></p><p><span style=\" font-size:9pt;\">Para usar cualquiera de ellos, simplemente coloque el cursor sobre ellos y presione el bot\u00f3n izquierdo, las funciones aparecer\u00e1n en la l\u00ednea principal de edici\u00f3n, luego coloque su n\u00famero y presione el bot\u00f3n &quot;=&quot;. Este procedimiento funciona para cualquiera de ellos.</span><br/></p></body></html>", None))
        self.help_tab_widgets.setTabText(self.help_tab_widgets.indexOf(self.calculator_help_tab), QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.help_manual_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Caj\u00f3n manual de procedimientos</span></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo usarlo?</span></p><p><span style=\" font-size:10pt;\">Este pintor trabaja solo con las cuatro operaciones b\u00e1sicas, usa el algoritmo que usamos cuando est\u00e1bamos en la etapa escolar, tambi\u00e9n es \u00fatil para los ni\u00f1os y tus hijos (si los tienes).</span></p><p><span style=\" font-size:10pt;\">Pasos</span></p><p><br/></p><p><span style=\" font-size:9pt;\">1. Primero, configure su operaci\u00f3n seleccion\u00e1ndola en la Lista de opciones mostradas (en caso de que no lo haya hecho, la operaci\u00f3n se seleccionar\u00e1 autom\u00e1ticamente.</span></p><p><span style=\" font-size:9pt;\">2. Aseg\u00farate de que en la opci\u00f3n Multiplicar solo tienes dos n\u00fameros, de lo contrario la operaci\u00f3n no ser\u00e1 como pretend\u00edas.</span></p><p><span style=\" font-size:9pt;\">3. Presione "
                        "el bot\u00f3n &quot;Obtener resultado&quot; y vea el procedimiento. Si nota alg\u00fan problema o inconsistencia, h\u00e1ganoslo saber a trav\u00e9s de la secci\u00f3n de preguntas frecuentes en la p\u00e1gina web de Shangoo.</span></p></body></html>", None))
        self.help_tab_widgets.setTabText(self.help_tab_widgets.indexOf(self.manual_help_tab), QCoreApplication.translate("MainWindow", u"Manual", None))
        self.help_conversions_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Conversi\u00f3n de medidas</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfQu\u00e9 es la secci\u00f3n &quot;Conversiones&quot;?</span></p><p><span style=\" font-size:9pt;\">Las secciones de conversiones son solo una herramienta para convertir la medida m\u00e1s utilizada en todo el mundo, por ejemplo, cent\u00edmetros en metros. Tambi\u00e9n puede seleccionar la medida que necesita, no solo la medida de longitud.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo usarlo?</span></p><p><span style=\" font-size:9pt;\">Esta herramienta est\u00e1 formada por tres subsectores:</span></p><p><span style=\" font-size:9pt;\">- Medida principal</span></p><p><span style=\" font-size:9pt;\">- Primera medida</span></p><p><span style=\" font-size:9pt;\">- Segundo comp\u00e1s</span></p><p><span style=\" font-size:9pt;\">- Marco de definici\u00f3n</s"
                        "pan></p><p><span style=\" font-size:9pt; font-weight:600;\">Medida principal</span></p><p><span style=\" font-size:9pt;\">En esta secci\u00f3n es donde seleccionar\u00e1s y elegir\u00e1s la medida con la que trabajar, est\u00e1 ubicada en la parte superior y hay un ComboBox con la medida a elegir.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">Primera medida</span></p><p><span style=\" font-size:9pt;\">Esta parte se reduce a la subsecci\u00f3n &quot;Medida principal&quot;. Aqu\u00ed es donde elegir\u00e1 la medida de la medida y luego insertar\u00e1 el n\u00famero para convertir.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">Segundo comp\u00e1s</span></p><p><span style=\" font-size:9pt;\">Esta secci\u00f3n funciona casi igual que la Primera, espere que no pueda escribir all\u00ed, y el resultado de la conversi\u00f3n se mostrar\u00e1 en ella, tambi\u00e9n puede elegir la medida para convertir.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">Marco de definici\u00f3n<"
                        "/span></p><p><span style=\" font-size:9pt;\">Dentro de esto, leer\u00e1 la definici\u00f3n de la medida y alimentar\u00e1 su mente con un gramo de un nuevo conocimiento.</span></p></body></html>", None))
        self.help_tab_widgets.setTabText(self.help_tab_widgets.indexOf(self.conversions_help_tab), QCoreApplication.translate("MainWindow", u"Conversions", None))
        self.help_settings_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Ayuda de configuraci\u00f3n</span></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfQu\u00e9 hay en la configuraci\u00f3n?</span></p><p><span style=\" font-size:10pt;\">Por lo general, en la configuraci\u00f3n, puede encontrar algunas opciones para cambiar y modificar Shangoo a su gusto. Puede cambiar el idioma, las unidades de medida de \u00e1ngulos, adem\u00e1s puede cambiar las preferencias para una experiencia m\u00e1s personalizada en la aplicaci\u00f3n Shangoo.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo configurar el idioma?</span></p><p><span style=\" font-size:10pt;\">Configurar o establecer el idioma es tan simple como abrir el men\u00fa lateral presionando el bot\u00f3n de men\u00fa.</span></p><p><span style=\" font-size:10pt;\">1. Ir a ayudar</span></p><p><span style=\" font-size:10pt;\">2. Presione el bot\u00f3n &quot;Configuraci\u00f3n&quot;.</span><"
                        "/p><p><span style=\" font-size:10pt;\">3. Vaya a la pesta\u00f1a &quot;idioma&quot;.</span></p><p><span style=\" font-size:10pt;\">4. Seleccione el necesario.</span></p><p><span style=\" font-size:10pt;\">5. Aplicar los cambios.</span></p><p><br/></p><p><span style=\" font-size:10pt;\">Adem\u00e1s, puede agregar cualquier idioma que desee insertando un archivo json en el archivo &quot;languages&quot;. Por defecto, Shangoo tiene idioma ingl\u00e9s y espa\u00f1ol, por cierto, el archivo json debe contener las mismas claves que los originales.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">\u00bfC\u00f3mo cambio las unidades de medida de los \u00e1ngulos?</span></p><p><span style=\" font-size:10pt;\">Como siempre, este proceso ser\u00e1 muy sencillo.</span></p><p><span style=\" font-size:10pt;\">1. Solo tienes que acceder a la Ayuda</span></p><p><span style=\" font-size:10pt;\">2. Presione el bot\u00f3n &quot;Configuraci\u00f3n&quot;</span></p><p><span style=\" font-size:10pt;\">3. Vay"
                        "a a la pesta\u00f1a &quot;Unidades de medida de \u00e1ngulos&quot;.</span></p><p><span style=\" font-size:10pt;\">4. Seleccione la medida que desea</span></p><p><span style=\" font-size:10pt;\">5. Y aplicar cambios</span></p><p><br/></p><p><span style=\" font-size:10pt;\">No es necesario reiniciar Shangoo y los cambios se guardar\u00e1n hasta la pr\u00f3xima vez.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Macros o teclas, \u00bfc\u00f3mo usarlas?</span></p><p><span style=\" font-size:10pt;\">\u00bfAlguna vez ha necesitado guardar un resultado o valor para usarlo despu\u00e9s ?, estas funciones le ayudar\u00e1n con este problema. Cada vez que necesite mantener un resultado sin perderlo, simplemente gu\u00e1rdelo en la lista de Macros. Hay cinco agujeros para que guardes tus resultados.</span></p><p><span style=\" font-size:10pt;\">1. Acceda a Ayuda, en el men\u00fa</span></p><p><span style=\" font-size:10pt;\">2. Seleccione la pesta\u00f1a &quot;Macros&quot;</span></p><p><span st"
                        "yle=\" font-size:10pt;\">3. Ver\u00e1 una tabla con la lista de macros, simplemente pegue su resultado en la celda y listo, puede usarlo entonces.</span></p><p><span style=\" font-size:10pt;\">4. Adem\u00e1s, si lo necesita, presione el bot\u00f3n &quot;Guardar macros&quot;; de lo contrario, sus macros no se guardar\u00e1n la pr\u00f3xima vez que ejecute Shangoo.</span></p><p><span style=\" font-size:10pt;\">5. Siempre que necesite usar alguna de los macros de la lista, selecci\u00f3nelo y presione &quot;Usar macro seleccionado&quot;, ver\u00e1 el macro en la linea de Edici\u00f3n principal, \u00a1Puede hacer lo que quiera con ellos!</span></p><p><span style=\" font-size:10pt;\">Tambi\u00e9n puede restablecer las macros en la configuraci\u00f3n predeterminada, por cierto, tambi\u00e9n debe guardar los cambios.</span></p><p><br/></p><p><span style=\" font-size:10pt; font-weight:600;\">Preferences</span></p><p><span style=\" font-size:10pt;\">The preferences are a series of options that allow you to configure so"
                        "me sections of the application, for this occasion doing so will be quite simple by following the following steps.</span></p><p><span style=\" font-size:10pt;\">1. Identify the option you want to change</span></p><p><span style=\" font-size:10pt;\">2. Check or uncheck the box of the desired option</span></p><p><span style=\" font-size:10pt;\">3. Press the &quot;apply&quot; button</span></p><p><span style=\" font-size:10pt;\">From now on the changes will be applied, it is not necessary to restart the application.</span></p></body></html>", None))
        self.help_tab_widgets.setTabText(self.help_tab_widgets.indexOf(self.settings_help_tab), QCoreApplication.translate("MainWindow", u"Setttings", None))
        self.disp_menu_btn.setText("")
        self.min_btn.setText("")
        self.restore_size_btn.setText("")
        self.close_btn.setText("")
        self.second_results_line.setText("")
        self.results_line.setText("")
        self.C_btn.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.multiply_btn.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.div_btn.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.dot_btn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.result_btn.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.porcent_btn.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.plus_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.tabWidget_btns.setTabText(self.tabWidget_btns.indexOf(self.standar), QCoreApplication.translate("MainWindow", u"Standar", None))
        self.one_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.abs.setText(QCoreApplication.translate("MainWindow", u"| X |", None))
        self.npr.setText(QCoreApplication.translate("MainWindow", u"nPr", None))
        self.one_div_x.setText(QCoreApplication.translate("MainWindow", u"1/X", None))
        self.ten_power10.setText(QCoreApplication.translate("MainWindow", u"10\u207f", None))
        self.euler.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.closed_bracket.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.eight_2.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.multiply.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pi.setText("")
        self.logy.setText(QCoreApplication.translate("MainWindow", u"log y\u207f", None))
        self.result.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.x_power2.setText(QCoreApplication.translate("MainWindow", u"X\u00b2", None))
        self.cb_root.setText("")
        self.two_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.C_btn_2.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.three_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.factorial.setText(QCoreApplication.translate("MainWindow", u"N!", None))
        self.ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.seven_2.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.back_btn_2.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.zero_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.two_powerx.setText(QCoreApplication.translate("MainWindow", u"2\u207f", None))
        self.four_2.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minus_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.plus_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.x_power3.setText(QCoreApplication.translate("MainWindow", u"X\u00b3", None))
        self.open_bracket.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.ncr.setText(QCoreApplication.translate("MainWindow", u"nCr", None))
        self.eng_p.setText(QCoreApplication.translate("MainWindow", u"ENG +", None))
        self.five_2.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.six_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.eng_m.setText(QCoreApplication.translate("MainWindow", u"ENG -", None))
        self.divide_btn.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.e_powerx.setText(QCoreApplication.translate("MainWindow", u"e\u207f", None))
        self.nine_2.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.sq_root.setText("")
        self.x_yroot.setText("")
        self.x_powery.setText(QCoreApplication.translate("MainWindow", u"x\u207f", None))
        self.tabWidget_btns.setTabText(self.tabWidget_btns.indexOf(self.science), QCoreApplication.translate("MainWindow", u"Science", None))
        self.four_3.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.csc_btn.setText(QCoreApplication.translate("MainWindow", u"csc", None))
        self.pi_2.setText("")
        self.euler_2.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.two_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.ctg_btn.setText(QCoreApplication.translate("MainWindow", u"ctg", None))
        self.nine_3.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.sin_btn.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.one_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.six_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.cos_btn.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.sec_btn.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.dot_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.tan_btn.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.five_3.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.zero_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.eight_3.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.seven_3.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.three_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.back_btn_3.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.C_btn_3.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.arcsin.setText(QCoreApplication.translate("MainWindow", u"sin\u207b\u00b9", None))
        self.arcos.setText(QCoreApplication.translate("MainWindow", u"cos\u207b\u00b9", None))
        self.arctan.setText(QCoreApplication.translate("MainWindow", u"tan\u207b\u00b9", None))
        self.multiply_btn_3.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.div_btn_3.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.minus_btn2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.plus_btn_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.result_3.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.tabWidget_btns.setTabText(self.tabWidget_btns.indexOf(self.trigo), QCoreApplication.translate("MainWindow", u"Trigonometry", None))
        self.historial_label.setText(QCoreApplication.translate("MainWindow", u"There's no operations yet", None))
        self.reset_historial_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.manual_tab.setTabText(self.manual_tab.indexOf(self.historial_frame), QCoreApplication.translate("MainWindow", u"Historial", None))
        self.select_operation_title.setText(QCoreApplication.translate("MainWindow", u"Select operation", None))
        self.select_operation_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sum", None))
        self.select_operation_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Subtraction", None))
        self.select_operation_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Multiply", None))
        self.select_operation_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Division", None))

        self.insert_exp_title.setText(QCoreApplication.translate("MainWindow", u"Insert expression", None))
        self.expression_lineEdit.setText("")
        self.get_draw_manual_btn.setText(QCoreApplication.translate("MainWindow", u"Get result", None))
        self.drawing_frame.setText(QCoreApplication.translate("MainWindow", u"Waiting for a expression...", None))
        self.clear_manual_frame.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.manual_tab.setTabText(self.manual_tab.indexOf(self.manual_frame), QCoreApplication.translate("MainWindow", u"Manual", None))
        self.convertions_head_label.setText(QCoreApplication.translate("MainWindow", u"Select one", None))
        self.convertions_measure_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Volume", None))
        self.convertions_measure_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Lenght", None))
        self.convertions_measure_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Weight", None))
        self.convertions_measure_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.convertions_measure_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.convertions_measure_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Time", None))
        self.convertions_measure_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Power", None))
        self.convertions_measure_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Data", None))
        self.convertions_measure_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Angle", None))

        self.convertions_body_top_label1.setText(QCoreApplication.translate("MainWindow", u"Convertion 1", None))
        self.convertions_body_top_lineEdit.setText("")
        self.convertions_body_top_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert value", None))
        self.convertions_body_down_label1.setText(QCoreApplication.translate("MainWindow", u"Convertion 2", None))
        self.convertions_body_down_label2.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.convertions_body_right_frame_top_title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.convertions_body_right_frame_down_label1.setText(QCoreApplication.translate("MainWindow", u"Definition:", None))
        self.convertions_body_right_frame_down_label2.setText(QCoreApplication.translate("MainWindow", u"Text body", None))
        self.manual_tab.setTabText(self.manual_tab.indexOf(self.conversions_tab), QCoreApplication.translate("MainWindow", u"Conversions", None))
        self.coming_soon.setText(QCoreApplication.translate("MainWindow", u"Coming Soon!", None))
        self.manual_tab.setTabText(self.manual_tab.indexOf(self.graphics_frame), QCoreApplication.translate("MainWindow", u"Graphics", None))
    # retranslateUi

