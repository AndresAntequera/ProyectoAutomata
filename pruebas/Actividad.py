# Desarrolle un programa en Python que resuelta A a la 5 aplicando la teoría de los lenguajes formales.


conjunto_a = {'#','ac','b'}
def elevadoconjunto(conjunto,valor):
    if(valor<=2):
        elevado = [(i, j) for i in conjunto for j in conjunto]
        return elevado
    else:
        return [(i, j) for i in conjunto for j in elevadoconjunto(conjunto,valor=valor-1)]

print('El conjunto elevado a la 1 es:',elevadoconjunto(conjunto_a,1))
print('----------------------------')
print('El conjunto elevado a la 2 es:',elevadoconjunto(conjunto_a,2))
print('----------------------------')
print('El conjunto elevado a la 3 es:',elevadoconjunto(conjunto_a,3))
print('----------------------------')
print('El conjunto elevado a la 4 es:',elevadoconjunto(conjunto_a,4))
print('----------------------------')
print('El conjunto elevado a la 5 es:',elevadoconjunto(conjunto_a,5))