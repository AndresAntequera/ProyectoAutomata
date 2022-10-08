# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
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
        MainWindow.resize(857, 699)
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
        icon.addFile(u"assets/MENU.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(441, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


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
        icon1 = QIcon()
        icon1.addFile(u"assets/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BotonInicio.setIcon(icon1)
        self.BotonInicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.BotonInicio)

        self.Buscador = QPushButton(self.lateral)
        self.Buscador.setObjectName(u"Buscador")
        self.Buscador.setMinimumSize(QSize(0, 40))
        self.Buscador.setMaximumSize(QSize(16777215, 40))
        icon2 = QIcon()
        icon2.addFile(u"assets/LUPA.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Buscador.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u"assets/Espa\u00f1a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Spanish.setIcon(icon3)
        self.Spanish.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Spanish)

        self.English = QPushButton(self.lateral)
        self.English.setObjectName(u"English")
        self.English.setMinimumSize(QSize(0, 40))
        self.English.setMaximumSize(QSize(16777215, 40))
        icon4 = QIcon()
        icon4.addFile(u"assets/USA.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.English.setIcon(icon4)
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
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_4 = QVBoxLayout(self.page1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.imagenrobot = QPushButton(self.page1)
        self.imagenrobot.setObjectName(u"imagenrobot")
        self.imagenrobot.setStyleSheet(u"background-color: rgb(55, 150, 131);")
        icon5 = QIcon()
        icon5.addFile(u"assets/robot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imagenrobot.setIcon(icon5)
        self.imagenrobot.setIconSize(QSize(500, 500))

        self.verticalLayout_4.addWidget(self.imagenrobot)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_5 = QVBoxLayout(self.page2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MarcoDerecho = QFrame(self.page2)
        self.MarcoDerecho.setObjectName(u"MarcoDerecho")
        self.MarcoDerecho.setStyleSheet(u"background-color: rgb(55, 150, 131);")
        self.MarcoDerecho.setFrameShape(QFrame.StyledPanel)
        self.MarcoDerecho.setFrameShadow(QFrame.Raised)
        self.BotonBuscar = QPushButton(self.MarcoDerecho)
        self.BotonBuscar.setObjectName(u"BotonBuscar")
        self.BotonBuscar.setGeometry(QRect(440, 90, 74, 40))
        self.BotonBuscar.setMinimumSize(QSize(0, 40))
        self.BotonBuscar.setMaximumSize(QSize(16777215, 40))
        self.BotonBuscar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"front: 87 12pt \"Arial Black\";\n"
"}\n"
"")
        self.BotonBuscar.setIcon(icon2)
        self.Etiqueta = QLabel(self.MarcoDerecho)
        self.Etiqueta.setObjectName(u"Etiqueta")
        self.Etiqueta.setGeometry(QRect(60, 10, 491, 61))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Etiqueta.setFont(font2)
        self.Etiqueta.setStyleSheet(u"QLabel{\n"
"border:0px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"front: 87 12pt \"Arial Black\";\n"
"}\n"
"")
        self.Etiqueta.setAlignment(Qt.AlignCenter)
        self.RespuestAN = QLabel(self.MarcoDerecho)
        self.RespuestAN.setObjectName(u"RespuestAN")
        self.RespuestAN.setGeometry(QRect(80, 136, 351, 20))
        self.RespuestAN.setAlignment(Qt.AlignCenter)
        self.BuscarPalabra = QLineEdit(self.MarcoDerecho)
        self.BuscarPalabra.setObjectName(u"BuscarPalabra")
        self.BuscarPalabra.setGeometry(QRect(80, 100, 351, 21))
        self.BuscarPalabra.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.MarcoDerecho)

        self.stackedWidget.addWidget(self.page2)

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
        self.BotonInicio.setText(QCoreApplication.translate("MainWindow", u"  INICIO", None))
        self.Buscador.setText(QCoreApplication.translate("MainWindow", u"BUSCADOR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"               IDIOMA", None))
        self.Spanish.setText(QCoreApplication.translate("MainWindow", u"   ESPA\u00d1OL", None))
        self.English.setText(QCoreApplication.translate("MainWindow", u"   INGLES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trabajo - Automata", None))
        self.imagenrobot.setText("")
        self.BotonBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Etiqueta.setText(QCoreApplication.translate("MainWindow", u"Automata de la expresion |   A*(B U C)*", None))
        self.RespuestAN.setText("")
        self.BuscarPalabra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insertar la palabra que desea buscar", None))
    # retranslateUi

