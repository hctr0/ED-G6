from Nodo import *
from ListNodes import *
if __name__ == "__main__":
    nodo = Nodo("new")
    listaNodos = ListNodes(nodo)
    listaNodos.agregarNodo("new2")
    listaNodos.agregarNodo("new3")
    listaNodos.agregarNodo("new4")
    #listaNodos.retornarUltimoNodo(nodo)
    for i in range(4):
        print(listaNodos.devolverNodo(i))
    print(listaNodos.retornarTamano())