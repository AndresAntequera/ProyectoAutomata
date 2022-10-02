#----------------------------

import re
texto = input()
print(re.search("Hola",texto)) 
# El search es para buscar una palabra en si

#----------------------------

# import re
# texto = input()
# print(re.findall("is",texto)) 

# Es para encontrar las susb cadenas en una expresion
# Me regresa una lista

#-----------------------------

# Es parecido al findall pero retorna un objeto iterator, 
# obtiene objetos tipo match

# import re
# texto = input()
# i = 0
# for item in re.finditer("is",texto):
#     print(item,i)
#     i+=1


#----------------------------
# Metacaracteres
# Conjuntos [] Pueden ser numeros o letras pero no ambos a la vez

# import re
# texto = input()
# print(re.findall("[0-7]",texto)) 

#----------------------------
# El . es para cualquiera caracter
# excepto saltos de linea

# import re
# texto = input()
# print(re.findall("....ar",texto))

#----------------------------
# Signo de potencia / ALT 94
# Es para que al inicio de la cadena 
# (Se cumpla lo que este despues)
# Ojo con las mayusculas

# import re
# texto = input()
# print(re.findall("^[A-Z]",texto))

#----------------------------
# Signo de dolar / esto significa 
# Que una cadena termine en tal 
# ejemplo:

# import re
# texto = input()
# print(re.findall("\w+@gmail.com$",texto))

#----------------------------
# Signo de operacion logica OR / | 
# Se usa para aplicarse en 2 conjuntos

# A = {'a','b','c'}
# B = {'c','d','e'}

# OR = A | B
# print(OR)
#----------------------------
 # Metacaracter 
 # * es para 0 o mas repeticiones
 # + es para 1 o mas repeticiones 

# import re
# texto = input()
# print(re.findall(".+er",texto))


# para quitar los espacios, debo de aplicar un conjunto

# import re
# texto = input()
# print(re.findall("[a-z]+er",texto))

#----------------------------
 # Metacaracter 
# Llaves {}  es para un numero exacto de repeticiones. Puede tener numero maximo y minimo 

# Ejemplo 

# import re
# texto = input()
# print(re.findall("[a-z]{4}er",texto))
#Comer, correr, barre

#----------------------------
# Signo de interrogacion ? es para 0 o 1 repeticion. Pero prioriza el minimo

# import re
# texto = input()
# print(re.findall("[a-z]?er",texto))

# #Comer, correr, barre

#----------------------------

# Parentesis () para capturar y agrupar/ lista de duplas para agrupar en grupos distintos
# #Ejemplo    

# import re
# texto = input()
# print(re.findall("([a-z]{4})(er)",texto))

# Comer, correr, barrer

#----------------------------