from resources.Nodo import *
class ListNodes:
    def __init__(self,data):
        self.Nodo = Nodo(data)
        self.tam =1
        self.head =self.Nodo

    def agregarNodo(self,data, nodo2 = None):
        node =Nodo(data)
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
    def retornarUltimoNodo(self, nodo2=None):
        if(self.Nodo.siguiente == None):
            print(self.Nodo.data)
        else:
            if(nodo2 !=None):
                if(nodo2.siguiente==None):
                    print(nodo2.data)
                    return
                else:
                    self.retornarUltimoNodo(nodo2.siguiente)    
            else:
                self.retornarUltimoNodo(self.Nodo.siguiente)
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
                nodo.data=None
                self.tam-=1
                return
            else:
                nodo = nodo.siguiente
                i+=1
