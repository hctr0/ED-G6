from resources.Nodo import *


class ListNodes:
    def __init__(self,data):
        self.Nodo = Nodo(data)
        self.tam =1
        self.head =self.Nodo
        self.tail =self.Nodo.siguiente

    #AGREGA UN NODO Y AUMENTA EN 1 SU TAMAÑO
    def agregarNodo(self,data):
        node = Nodo(data)
        if(self.Nodo.siguiente == None):
            self.Nodo.siguiente = node
            self.tam +=1
            return
        else:
            nodo1 = self.Nodo
            acceso = True
            while(acceso):
                if(nodo1.siguiente == None):
                    nodo1.siguiente=node
                    self.tail = node
                    self.tam += 1
                    return
                else:
                    nodo1 = nodo1.siguiente
            
    def retornarUltimoNodo(self):
        return self.tail.data
            
    def retornarTamano(self):
        return self.tam
    def devolverData(self, posicion):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                return nodo.data
            else:
                nodo = nodo.siguiente
                i+=1
    def devolverNodo(self, posicion):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                return nodo
            else:
                nodo = nodo.siguiente
                i+=1
    def editarNodo(self, posicion, value):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                nodo.data=value
                return
            else:
                nodo = nodo.siguiente
                i+=1
    def eliminarNodo(self, posicion):
        nodo = self.Nodo
        i = 0
        while(i<self.tam):
            if(i==posicion):
                if(nodo.siguiente != None):
                    if(posicion!=0):
                        nodo2=self.devolverNodo(posicion-1)
                        nodo2.siguiente =nodo.siguiente
                    else:
                        self.head = nodo.siguiente
                if(nodo.data == self.tail.data):
                    self.tail =self.devolverNodo(posicion-1)
                nodo.data=None
                self.tam-=1
                return
            else:
                nodo = nodo.siguiente
                i+=1
