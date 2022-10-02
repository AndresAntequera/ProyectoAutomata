# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Automata.ui'
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
        MainWindow.resize(800, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color: rgb(58, 175, 169);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 35))
        self.bt_menu.setMaximumSize(QSize(16777215, 35))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: #3AAFA9;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/MENU.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(441, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#7a7a7a;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/Minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_restaurar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#4423ff;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ff0004;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../assets/cerrar2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lateral = QFrame(self.frame_inferior)
        self.lateral.setObjectName(u"lateral")
        self.lateral.setMinimumSize(QSize(200, 25))
        self.lateral.setMaximumSize(QSize(0, 16777215))
        self.lateral.setStyleSheet(u"QFrame{\n"
"background-color:#2B7A78;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#2B7A78;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font: 75 12pt\"Arial Narrow\";\n"
"}")
        self.lateral.setFrameShape(QFrame.StyledPanel)
        self.lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BotonInicio = QPushButton(self.lateral)
        self.BotonInicio.setObjectName(u"BotonInicio")
        self.BotonInicio.setMinimumSize(QSize(0, 40))
        self.BotonInicio.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u"../assets/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonInicio.setIcon(icon5)
        self.BotonInicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BotonInicio)

        self.Buscador = QPushButton(self.lateral)
        self.Buscador.setObjectName(u"Buscador")
        self.Buscador.setMinimumSize(QSize(0, 40))
        self.Buscador.setMaximumSize(QSize(16777215, 40))
        icon6 = QIcon()
        icon6.addFile(u"../assets/LUPA.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Buscador.setIcon(icon6)
        self.Buscador.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Buscador)

        self.label_3 = QLabel(self.lateral)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.Spanish = QPushButton(self.lateral)
        self.Spanish.setObjectName(u"Spanish")
        self.Spanish.setMinimumSize(QSize(0, 40))
        self.Spanish.setMaximumSize(QSize(16777215, 40))
        icon7 = QIcon()
        icon7.addFile(u"../assets/Espa\u00f1a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spanish.setIcon(icon7)
        self.Spanish.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Spanish)

        self.English = QPushButton(self.lateral)
        self.English.setObjectName(u"English")
        self.English.setMinimumSize(QSize(0, 40))
        self.English.setMaximumSize(QSize(16777215, 40))
        icon8 = QIcon()
        icon8.addFile(u"../assets/USA.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.English.setIcon(icon8)
        self.English.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.English)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.lateral)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushbutton = QPushButton(self.page)
        self.pushbutton.setObjectName(u"pushbutton")
        self.pushbutton.setStyleSheet(u"background-color: rgb(55, 150, 131);")
        icon9 = QIcon()
        icon9.addFile(u"../assets/robot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton.setIcon(icon9)
        self.pushbutton.setIconSize(QSize(500, 500))

        self.verticalLayout_4.addWidget(self.pushbutton)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(55, 150, 131);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 110, 74, 41))
        self.pushButton_2.setMaximumSize(QSize(74, 16777215))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(222, 242, 241);")
        self.pushButton_2.setIcon(icon6)
        self.Etiqueta = QLabel(self.frame)
        self.Etiqueta.setObjectName(u"Etiqueta")
        self.Etiqueta.setGeometry(QRect(10, 100, 461, 61))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Etiqueta.setFont(font2)
        self.Etiqueta.setAlignment(Qt.AlignCenter)
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 200, 471, 171))
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.BotonInicio.setText(QCoreApplication.translate("MainWindow", u"  INICIO", None))
        self.Buscador.setText(QCoreApplication.translate("MainWindow", u"BUSCADOR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"               IDIOMA", None))
        self.Spanish.setText(QCoreApplication.translate("MainWindow", u"   ESPA\u00d1OL", None))
        self.English.setText(QCoreApplication.translate("MainWindow", u"   INGLES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trabajo - Automata", None))
        self.pushbutton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Etiqueta.setText(QCoreApplication.translate("MainWindow", u"Inserte la palabra que desea buscar", None))
    # retranslateUi

