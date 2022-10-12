from time import sleep
from PyQt5 import QtWidgets,QtGui,uic,QtCore
from PyQt5.QtCore import QPropertyAnimation,QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from Grafo import buscar,grafo 


# import QtMultimedia

app = QtWidgets.QApplication([])
inicio = uic.loadUi("inicio.ui")
buscador = uic.loadUi("buscador.ui")
inicioIngles = uic.loadUi("inicioIngles.ui")
BuscadorIngles= uic.loadUi("BuscadorIngles.ui")



def Vinicio():
    buscador.hide()
    inicio.show()
    inicioIngles.hide()
    BuscadorIngles.hide()
            
def Vbuscar():
    inicio.hide()
    buscador.show()
    
def VinicioIngles():
    inicio.hide()
    buscador.hide()
    inicioIngles.show()
    BuscadorIngles.hide()
    
def VBuscadorIngles():
    inicioIngles.hide()
    buscador.hide()
    BuscadorIngles.show()
    
    
    
#BuscadorEspañol
    
inicio.Buscador.clicked.connect(Vbuscar)
inicio.English.clicked.connect(VinicioIngles)
buscador.BotonInicio.clicked.connect(Vinicio)
buscador.English.clicked.connect(VBuscadorIngles)


# BuscadorIngles.
inicioIngles.Spanish.clicked.connect(Vinicio)
inicioIngles.Buscador.clicked.connect(VBuscadorIngles)
BuscadorIngles.BotonInicio.clicked.connect(VinicioIngles)
BuscadorIngles.Spanish.clicked.connect(Vinicio)




def buscar_palabra():
    palabra = buscador.BuscarPalabra.text()
    estado = buscar(grafo,palabra.upper())

    if buscador.Radio3.isChecked():
        mostrarTransicion(grafo,palabra.upper(),0.2)
    elif buscador.Radio1.isChecked():
        mostrarTransicion(grafo,palabra.upper(),1.3)
    elif buscador.Radio2.isChecked():
        mostrarTransicion(grafo,palabra.upper(),0.6)
    else:
        mostrarTransicion(grafo,palabra.upper(),0.6)


    if estado == "aceptado":
        buscador.RespuestAN.setText("ACEPTADO")
    else:
        buscador.RespuestAN.setText("DENEGADO")
        

buscador.BotonBuscar.clicked.connect(buscar_palabra)


def buscar_palabraIngles():
    palabra = BuscadorIngles.BuscarPalabra.text()
    estado = buscar(grafo,palabra.upper())

    if BuscadorIngles.RadioIngles3.isChecked():
        mostrarTransicionIngles(grafo,palabra.upper(),0.2)
    elif BuscadorIngles.RadioIngles1.isChecked():
        mostrarTransicionIngles(grafo,palabra.upper(),1.3)
    elif BuscadorIngles.RadioIngles2.isChecked():
        mostrarTransicionIngles(grafo,palabra.upper(),0.6)
    else:
        mostrarTransicionIngles(grafo,palabra.upper(),0.6)


    if estado == "aceptado":
        BuscadorIngles.RespuestaIngles.setText("ACCEPTED")
    else:
        BuscadorIngles.RespuestaIngles.setText("DENIED")
        
BuscadorIngles.BotonBuscar.clicked.connect(buscar_palabraIngles)


#Primer Nodo español
label_1 = buscador.Q0 
label_1.move(100, 220) 
label_1.resize(80, 80)
label_1.setAlignment(QtCore.Qt.AlignCenter)
label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_2 = buscador.Q0_2
label_2.move(95, 215)
label_2.resize(90,90)
label_2.setAlignment(QtCore.Qt.AlignCenter)
label_2.setStyleSheet("border: 3px solid black; border-radius: 45px;")

#Segundo Nodo español
label_3 = buscador.Q1
label_3.move(260, 60) 
label_3.resize(80, 80)
label_3.setAlignment(QtCore.Qt.AlignCenter)
label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_4 = buscador.Q1_2
label_4.move(255, 55)
label_4.resize(90,90)
label_4.setAlignment(QtCore.Qt.AlignCenter)
label_4.setStyleSheet("border: 3px solid black; border-radius: 45px;")

#Tercer Nodo español
label_5 = buscador.Q2
label_5.move(390, 220) 
label_5.resize(80, 80)
label_5.setAlignment(QtCore.Qt.AlignCenter)
label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_6 = buscador.Q2_2
label_6.move(385, 215)
label_6.resize(90,90)
label_6.setAlignment(QtCore.Qt.AlignCenter)
label_6.setStyleSheet("border: 3px solid black; border-radius: 45px;")

#ingles visualizador


#Primer Nodo ingles
label_1_ingles = BuscadorIngles.Q0 
label_1_ingles.move(100, 220) 
label_1_ingles.resize(80, 80)
label_1_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_2_ingles = BuscadorIngles.Q0_2
label_2_ingles.move(95, 215)
label_2_ingles.resize(90,90)
label_2_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_2_ingles.setStyleSheet("border: 3px solid black; border-radius: 45px;")

#Segundo Nodo ingles
label_3_ingles = BuscadorIngles.Q1
label_3_ingles.move(260, 60) 
label_3_ingles.resize(80, 80)
label_3_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_4_ingles = BuscadorIngles.Q1_2
label_4_ingles.move(255, 55)
label_4_ingles.resize(90,90)
label_4_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_4_ingles.setStyleSheet("border: 3px solid black; border-radius: 45px;")

#Tercer Nodo ingles
label_5_ingles = BuscadorIngles.Q2
label_5_ingles.move(390, 220) 
label_5_ingles.resize(80, 80)
label_5_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
label_6_ingles = BuscadorIngles.Q2_2
label_6_ingles.move(385, 215)
label_6_ingles.resize(90,90)
label_6_ingles.setAlignment(QtCore.Qt.AlignCenter)
label_6_ingles.setStyleSheet("border: 3px solid black; border-radius: 45px;")
                

def mostrarTransicion(grafo,palabra,veloz):
    contador = 0
    nodo = 0
    acumulado = ""
    
    
    if palabra == "":
        label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
        QtWidgets.QApplication.processEvents()
        sleep(veloz)
        label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
    else:
        for i in palabra:
            contador+=1
            if grafo.get_edge_data("q0","q1")['A']['attr'] == i and nodo==0:
                acumulado+=i
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1

                buscador.pushButton.setIcon(QtGui.QIcon('./assets/ABlanco.png'))
                buscador.pushButton.setIconSize(QtCore.QSize(130,100))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                buscador.pushButton.setIcon(QtGui.QIcon('./assets/AA.png'))
                buscador.pushButton.setIconSize(QtCore.QSize(130,100))


                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return
                else:
                    continue
            elif grafo.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1

                buscador.pushButton_2.setIcon(QtGui.QIcon('./assets/A.Blanco.png'))
                buscador.pushButton_2.setIconSize(QtCore.QSize(120,70))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                buscador.pushButton_2.setIcon(QtGui.QIcon('./assets/A.jpg'))
                buscador.pushButton_2.setIconSize(QtCore.QSize(120,70))

                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return
                else:
                    continue
            elif (grafo.get_edge_data("q1","q2")['B']['attr'] == i or grafo.get_edge_data("q1","q2")['C']['attr'] == i) and nodo == 1:
                acumulado+=i
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2

                if i == 'C' or i == 'c':
                    buscador.pushButton_5.setIcon(QtGui.QIcon('./assets/CBlanco.png'))
                    buscador.pushButton_5.setIconSize(QtCore.QSize(100,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    buscador.pushButton_5.setIcon(QtGui.QIcon('./assets/C.png'))
                    buscador.pushButton_5.setIconSize(QtCore.QSize(120,70))
                else:
                    buscador.pushButton_7.setIcon(QtGui.QIcon('./assets/BDBLANCO.png'))
                    buscador.pushButton_7.setIconSize(QtCore.QSize(60,100))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    buscador.pushButton_7.setIcon(QtGui.QIcon('./assets/BDerecho.png'))
                    buscador.pushButton_7.setIconSize(QtCore.QSize(60,100))

                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            elif (grafo.get_edge_data("q2","q2")['B']['attr'] == i or grafo.get_edge_data("q2","q2")['C']['attr'] == i) and nodo==2:
                acumulado+=i
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2
                
                buscador.pushButton_3.setIcon(QtGui.QIcon('./assets/BCBlanco.png'))
                buscador.pushButton_3.setIconSize(QtCore.QSize(100,80))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                buscador.pushButton_3.setIcon(QtGui.QIcon('./assets/BC.png'))
                buscador.pushButton_3.setIconSize(QtCore.QSize(100,80))

                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            elif (grafo.get_edge_data("q0","q2")['B']['attr'] == i or grafo.get_edge_data("q0","q2")['C']['attr'] == i) and nodo==0:
                acumulado+=i
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")

                nodo = 2

                if i == 'B' or i == 'b':
                    buscador.pushButton_4.setIcon(QtGui.QIcon('./assets/BBlanco.png'))
                    buscador.pushButton_4.setIconSize(QtCore.QSize(100,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    buscador.pushButton_4.setIcon(QtGui.QIcon('./assets/B.png'))
                    buscador.pushButton_4.setIconSize(QtCore.QSize(120,70))
                else:
                    buscador.pushButton_6.setIcon(QtGui.QIcon('./assets/C_inferiorBlanco.png'))
                    buscador.pushButton_6.setIconSize(QtCore.QSize(150,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    buscador.pushButton_6.setIcon(QtGui.QIcon('./assets/C_inferior.png'))
                    buscador.pushButton_6.setIconSize(QtCore.QSize(150,90))


                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            else:
                return 


def mostrarTransicionIngles(grafo,palabra,veloz):
    contador = 0
    nodo = 0
    acumulado = ""
    
    if palabra == "":
        label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
        QtWidgets.QApplication.processEvents()
        sleep(veloz)
        label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
    else:
        for i in palabra:
            contador+=1
            if grafo.get_edge_data("q0","q1")['A']['attr'] == i and nodo==0:
                acumulado+=i
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1

                BuscadorIngles.pushButton.setIcon(QtGui.QIcon('./assets/ABlanco.png'))
                BuscadorIngles.pushButton.setIconSize(QtCore.QSize(130,100))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                BuscadorIngles.pushButton.setIcon(QtGui.QIcon('./assets/AA.png'))
                BuscadorIngles.pushButton.setIconSize(QtCore.QSize(130,100))


                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return
                else:
                    continue
            elif grafo.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1

                BuscadorIngles.pushButton_2.setIcon(QtGui.QIcon('./assets/A.Blanco.png'))
                BuscadorIngles.pushButton_2.setIconSize(QtCore.QSize(120,70))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                BuscadorIngles.pushButton_2.setIcon(QtGui.QIcon('./assets/A.jpg'))
                BuscadorIngles.pushButton_2.setIconSize(QtCore.QSize(120,70))

                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return
                else:
                    continue
            elif (grafo.get_edge_data("q1","q2")['B']['attr'] == i or grafo.get_edge_data("q1","q2")['C']['attr'] == i) and nodo == 1:
                acumulado+=i
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo=2
                
                if i == 'C' or i == 'c':
                    BuscadorIngles.pushButton_5.setIcon(QtGui.QIcon('./assets/CBlanco.png'))
                    BuscadorIngles.pushButton_5.setIconSize(QtCore.QSize(100,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    BuscadorIngles.pushButton_5.setIcon(QtGui.QIcon('./assets/C.png'))
                    BuscadorIngles.pushButton_5.setIconSize(QtCore.QSize(120,70))
                else:
                    BuscadorIngles.pushButton_7.setIcon(QtGui.QIcon('./assets/BDBLANCO.png'))
                    BuscadorIngles.pushButton_7.setIconSize(QtCore.QSize(60,100))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    BuscadorIngles.pushButton_7.setIcon(QtGui.QIcon('./assets/BDerecho.png'))
                    BuscadorIngles.pushButton_7.setIconSize(QtCore.QSize(60,100))

                
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            elif (grafo.get_edge_data("q2","q2")['B']['attr'] == i or grafo.get_edge_data("q2","q2")['C']['attr'] == i) and nodo==2:
                acumulado+=i
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2
                
                BuscadorIngles.pushButton_3.setIcon(QtGui.QIcon('./assets/BCBlanco.png'))
                BuscadorIngles.pushButton_3.setIconSize(QtCore.QSize(100,80))
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                BuscadorIngles.pushButton_3.setIcon(QtGui.QIcon('./assets/BC.png'))
                BuscadorIngles.pushButton_3.setIconSize(QtCore.QSize(100,80))
                
                
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            elif (grafo.get_edge_data("q0","q2")['B']['attr'] == i or grafo.get_edge_data("q0","q2")['C']['attr'] == i) and nodo==0:
                acumulado+=i
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2
                
                if i == 'B' or i == 'b':
                    BuscadorIngles.pushButton_4.setIcon(QtGui.QIcon('./assets/BBlanco.png'))
                    BuscadorIngles.pushButton_4.setIconSize(QtCore.QSize(100,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    BuscadorIngles.pushButton_4.setIcon(QtGui.QIcon('./assets/B.png'))
                    BuscadorIngles.pushButton_4.setIconSize(QtCore.QSize(120,70))
                else:
                    BuscadorIngles.pushButton_6.setIcon(QtGui.QIcon('./assets/C_inferiorBlanco.png'))
                    BuscadorIngles.pushButton_6.setIconSize(QtCore.QSize(150,90))
                    QtWidgets.QApplication.processEvents()
                    sleep(veloz)
                    BuscadorIngles.pushButton_6.setIcon(QtGui.QIcon('./assets/C_inferior.png'))
                    BuscadorIngles.pushButton_6.setIconSize(QtCore.QSize(150,90))

                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == contador and acumulado==palabra:
                    return 
                else:
                    continue
            else:
                return 



inicio.show()
app.exec()
