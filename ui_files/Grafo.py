import networkx as nx
from attr import attr

grafo = nx.MultiGraph()


grafo.add_node("q0")
grafo.add_node("q1")
grafo.add_node("q2")


grafo.add_edge("q0","q0","",attr='')
grafo.add_edge("q0","q1","A",attr="A")
grafo.add_edge("q0","q2","B",attr="B")
grafo.add_edge("q0","q2","C",attr="C")
grafo.add_edge("q1","q1","A",attr="A")
grafo.add_edge("q1","q2","C",attr="C")
grafo.add_edge("q1","q2","B",attr="B")
grafo.add_edge("q2","q2","B",attr="B")
grafo.add_edge("q2","q2","C",attr="C")

def buscar(grafo,palabra):
    contador = 0
    nodo = 0
    acumulado = ""
    
    if palabra == "":
        return "aceptado"
    else:
        for i in palabra:
            contador+=1
            if grafo.get_edge_data("q0","q1")['A']['attr'] == i and contador==1:
                acumulado+=i
                nodo = 1
                if len(palabra) == contador and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif grafo.get_edge_data("q1","q1")['A']['attr'] == i and nodo==1:
                acumulado+=i
                nodo = 1
                if len(palabra) == contador and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif grafo.get_edge_data("q1","q2")['B']['attr'] == i or grafo.get_edge_data("q1","q2")['C']['attr'] == i and nodo==1:
                acumulado+=i
                nodo=2
                if len(palabra) == contador and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif grafo.get_edge_data("q2","q2")['B']['attr'] == i or grafo.get_edge_data("q2","q2")['C']['attr'] == i and nodo==2:
                acumulado+=i
                nodo = 2
                if len(palabra) == contador and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            elif grafo.get_edge_data("q0","q2")['B']['attr'] == i or grafo.get_edge_data("q0","q2")['C']['attr'] == i and contador==1 and nodo==0:
                acumulado+=i
                nodo = 2
                if len(palabra) == contador and acumulado==palabra:
                    return "aceptado"
                else:
                    continue
            else:
                return "denegado" 