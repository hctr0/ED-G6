from resources.Nodo import *
from resources.ListNodes import * 
if __name__ == "__main__":
    nodo = Nodo("new")
    listaNodos = ListNodes(nodo)
    listaNodos.agregarNodo("new2")
    listaNodos.agregarNodo("new3")
    listaNodos.agregarNodo("new4")
    listaNodos.agregarNodo("new5")
    listaNodos.agregarNodo("new6")
    listaNodos.agregarNodo("new7")
    listaNodos.agregarNodo("new8")
    listaNodos.agregarNodo("new9")
    listaNodos.agregarNodo("new10")
    #listaNodos.retornarUltimoNodo(nodo)
    for i in range(listaNodos.retornarTamano()):
        print(listaNodos.devolverNodo(i))
    print(listaNodos.retornarTamano())
    