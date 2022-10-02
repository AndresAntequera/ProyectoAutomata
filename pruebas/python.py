A = {'a','b','c'}
B = {'b','c','d'}

# union = A | B
# interseccion = A & B
# diferencia = B - A
# print(diferencia)
# print(len(A))

# operacion potencia
# pal = 'diego'
# print(pal*20)

# producto cruz o cartesiano
#    def productoCruz(conjunto1,conjunto2):
#         pCruz = [(i, j) for i in conjunto1 for j in conjunto2]
#        return pCruz
#            print(productoCruz(A,B))


lenguaje_a = {'diego','jose','luna'}
def potenciaLenguaje(lenguaje,valor):
    if(valor<=2):
        potencia = [(i, j) for i in lenguaje for j in lenguaje]
        return potencia
    else:
        return [(i, j) for i in lenguaje for j in potenciaLenguaje(lenguaje,valor=valor-1)]

print(potenciaLenguaje(lenguaje_a,5))


# longitud de un lenguaje
# print(len(lenguaje_a))


# inverso de un lenguaje
# print("".join(reversed("hola")))
# lenguaje_b = {'arbol','silla','nose'}
# def invertirLenguaje(lenguaje):
#     lenguajeAux = set()
#     # conjunto vacio, lenguajeAux = set() == lenguajeAux = {}
#     for i in lenguaje:
#         inversa = "".join(reversed(i))
#         lenguajeAux.add(inversa)
#     print(lenguajeAux)
        
# invertirLenguaje(lenguaje_b)


#Concatenar elementos
# conjuntoA = ['corr','beb']
# conjuntoB = ['er','o','imos']
# conjuntoC = []

# for elemento in conjuntoA:
#     for elemento2 in conjuntoB:
#         conjuntoC.append(elemento+elemento2)
# print(conjuntoC)