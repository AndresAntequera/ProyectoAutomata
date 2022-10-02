from __future__ import division
import tkinter as tk
from tkinter import END, Button, Entry, Image, ttk

i = 0

ventana = tk.Tk()
ventana.title("Calculadora")

entrada_texto = Entry(ventana, font = ("TimesNewRoman 20"),textvariable="0")
entrada_texto.grid(row=0,column=0,columnspan=4,pady=5)

def click_button(value):
    global i
    if(value=="x"):
        entrada_texto.insert(i, "*")
    else:
        entrada_texto.insert(i,value)
    
    
    i += 1 

def borrar():
    entrada_texto.delete(0,END)
    i=0

def hacer_operacion():
    operacion = entrada_texto.get()
    resultado = eval(operacion)
    entrada_texto.delete(0,END)
    entrada_texto.insert(0,resultado)
    i=0

#creacion botones
buttonAC = Button(ventana, text="AC",width=5,height=5,background="orange",borderwidth=0,command= lambda:borrar())
buttonParentesisC = Button(ventana, text=")",width=5,height=5,background="orange",borderwidth=0,command= lambda:click_button(")"))
buttonParentesisA = Button(ventana, text="(",width=5,height=5,background="orange",borderwidth=0,command= lambda:click_button("("))
buttonPunto = Button(ventana, text=".",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button("."))

num9 = Button(ventana, text="9",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(9)) 
num7 = Button(ventana, text="7",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(7)) 
num6 = Button(ventana, text="6",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(6)) 
num8 = Button(ventana, text="8",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(8)) 
num5 = Button(ventana, text="5",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(5)) 
num4 = Button(ventana, text="4",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(4)) 
num3 = Button(ventana, text="3",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(3)) 
num2 = Button(ventana, text="2",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(2)) 
num1 = Button(ventana, text="1",width=5,height=5,background="purple",borderwidth=0,command= lambda:click_button(1)) 
num0 = Button(ventana, text="0",width=16,height=5,background="purple",borderwidth=0,command= lambda:click_button(0))

division = Button(ventana, text="%",width=5,height=5,background="gray",borderwidth=0,command= lambda:click_button("%"))
suma = Button(ventana, text="+",width=5,height=5,background="gray",borderwidth=0,command= lambda:click_button("+"))
multiplicacion = Button(ventana, text="x",width=5,height=5,background="gray",borderwidth=0,command= lambda:click_button("x"))
resta = Button(ventana, text="-",width=5,height=5,background="gray",borderwidth=0,command= lambda:click_button("-"))
igual = Button(ventana, text="=",width=5,height=5,background="gray",borderwidth=0,command= lambda: hacer_operacion())

#posicionamiento
buttonAC.grid(row=1,column=0,pady=8)
buttonParentesisA.grid(row=1,column=1,pady=8)
buttonParentesisC.grid(row=1,column=2,pady=8)

division.grid(row=1,column=3,pady=8)
suma.grid(row=2,column=3,pady=8)
multiplicacion.grid(row=3,column=3,pady=8)
resta.grid(row=4,column=3,pady=8)
igual.grid(row=5,column=3,pady=8)

num9.grid(row=2,column=2,pady=8)
num8.grid(row=2,column=1,pady=8)
num7.grid(row=2,column=0,pady=8)
num6.grid(row=3,column=2,pady=8)
num5.grid(row=3,column=1,pady=8)
num4.grid(row=3,column=0,pady=8)
num3.grid(row=4,column=2,pady=8)
num2.grid(row=4,column=1,pady=8)
num1.grid(row=4,column=0,pady=8)
num0.grid(row=5,column=0,columnspan=2,pady=8)

buttonPunto.grid(row=5,column=2,pady=8)

ventana.mainloop()                     

