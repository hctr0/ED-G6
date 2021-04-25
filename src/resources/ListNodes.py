from resources.Nodo import *


class ListNodes:

    #CONSTRUCTOR DE CLASE
    def __init__(self,Nodo):
        self.Nodo = Nodo
        self.tam =1


    #AGREGA UN NODO Y AUMENTA EN 1 SU TAMAÑO
    def agregarNodo(self,data, nodo2 = None):
        node = Nodo(data)
        if(self.Nodo.siguiente == None):
            self.Nodo.siguiente = node
            self.tam +=1
            return
        else:
            if(nodo2 !=None):
                if(nodo2.siguiente==None):
                    nodo2.siguiente =node
                    self.tam +=1
                else:
                    self.agregarNodo(data,nodo2.siguiente)    
            else:
                self.agregarNodo(data,self.Nodo.siguiente)    
    

    #DEVUELVE EL ÚLTIMO NODO DE FORMA RECURSIVA
    def retornarUltimoNodo(self,nodo2 ):
        if(nodo2.siguiente == None):
            return nodo2.data
        else:
            self.retornarUltimoNodo(self.Nodo.siguiente)
    

    #DEVUELVE EL TAMAÑO DE LA LISTA EN O(1)
    def retornarTamano(self):
        return self.tam
    

    #DEVUELVE EL NODO EN UN DETERMINADO INDICE
    def devolverNodo(self, posicion):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                return nodo.data
            else:
                nodo = nodo.siguiente
                i+=1