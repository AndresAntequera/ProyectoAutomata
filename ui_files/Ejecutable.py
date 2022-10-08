from time import sleep
from turtle import width
from PyQt5 import QtWidgets,QtGui,uic,QtCore
from PyQt5.QtCore import QPropertyAnimation,QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from Grafo import buscar,g  
import sys,os


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
    estado = buscar(g,palabra.upper())
    
    mostrarTransicion(g,palabra.upper(),0.5)
        
    if estado == "aceptado":
        buscador.RespuestAN.setText("ACEPTADO")
    else:
        buscador.RespuestAN.setText("DENEGADO")
        
buscador.BotonBuscar.clicked.connect(buscar_palabra)


def Vlento():
    buscar_palabra(1)

def Vnormal():
    buscar_palabra(.5)

def Vrapido():
    buscar_palabra(.2)


    

buscador.lento.clicked.connect(Vlento)
buscador.normal.clicked.connect(Vnormal)
buscador.rapido.clicked.connect(Vrapido)

def buscar_palabraIngles():
    palabra = BuscadorIngles.BuscarPalabra.text()
    estado = buscar(g,palabra.upper())
    mostrarTransicionIngles(g,palabra.upper())
    if estado == "aceptado":
        BuscadorIngles.RespuestaIngles.setText("ACCEPTED")
    else:
        BuscadorIngles.RespuestaIngles.setText("DENIED")
        
BuscadorIngles.BotonBuscar.clicked.connect(buscar_palabraIngles)


#Primer Nodo
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

#Segundo Nodo
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

#Tercer Nodo
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


#Primer Nodo
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

#Segundo Nodo
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

#Tercer Nodo
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


# player = QMediaPlayer()
 
# def playAudioFile():
#         full_file_path = os.path.join(os.getcwd(), 'aceptado.mp3')
#         url = QUrl.fromLocalFile(full_file_path)
#         content = QMediaContent(url)

#         player.setMedia(content)
#         player.play()
                

def mostrarTransicion(g,palabra,veloz):
    c = 0
    nodo = 0
    acumulado = ""
    
    
    if palabra == "":
        label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
        QtWidgets.QApplication.processEvents()
        sleep(veloz)
        label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
    else:
        for i in palabra:
            c+=1
            if g.get_edge_data("q0","q1")['A']['attr'] == i and nodo==0:
                acumulado+=i
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return
                else:
                    continue
            elif g.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return
                else:
                    continue
            elif (g.get_edge_data("q1","q2")['B']['attr'] == i or g.get_edge_data("q1","q2")['C']['attr'] == i) and nodo == 1:
                acumulado+=i
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_3.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo=2
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            elif (g.get_edge_data("q2","q2")['B']['attr'] == i or g.get_edge_data("q2","q2")['C']['attr'] == i) and nodo==2:
                acumulado+=i
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2
                
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            elif (g.get_edge_data("q0","q2")['B']['attr'] == i or g.get_edge_data("q0","q2")['C']['attr'] == i) and nodo==0:
                acumulado+=i
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")

                nodo = 2
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(veloz)
                label_5.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            else:
                return 


def mostrarTransicionIngles(g,palabra):
    c = 0
    nodo = 0
    acumulado = ""
    
    if palabra == "":
        label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
        QtWidgets.QApplication.processEvents()
        sleep(1)
        label_1.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
    else:
        for i in palabra:
            c+=1
            if g.get_edge_data("q0","q1")['A']['attr'] == i and nodo==0:
                acumulado+=i
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return
                else:
                    continue
            elif g.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 1
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return
                else:
                    continue
            elif (g.get_edge_data("q1","q2")['B']['attr'] == i or g.get_edge_data("q1","q2")['C']['attr'] == i) and nodo == 1:
                acumulado+=i
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_3_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo=2
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            elif (g.get_edge_data("q2","q2")['B']['attr'] == i or g.get_edge_data("q2","q2")['C']['attr'] == i) and nodo==2:
                acumulado+=i
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                nodo = 2
                
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(.5)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            elif (g.get_edge_data("q0","q2")['B']['attr'] == i or g.get_edge_data("q0","q2")['C']['attr'] == i) and nodo==0:
                acumulado+=i
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_1_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")

                nodo = 2
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;background:#fff")
                QtWidgets.QApplication.processEvents()
                sleep(1)
                label_5_ingles.setStyleSheet("border: 3px solid black; border-radius: 40px; text-align:center;")
                if len(palabra) == c and acumulado==palabra:
                    return 
                else:
                    continue
            else:
                return 


inicio.show()
app.exec()