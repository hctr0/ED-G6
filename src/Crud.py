from src.resources.ListNodes import *
from src.resources.Arbolavl import *
from src.resources.hashtable import *
from src.resources.mapPrioridad import *
from .models import User
class Crud:
    #ESTA FUNCION ACTUALIZA UN DATO EN LA ESTRUCTURA
    def ActualizarDato(self, arbol, value):
        arbol.search(arbol.root, value)
    #FUNCION DISEÑADA PARA INSERTAR UN DATO
    def InsertDato(self, hash, data):
        user = mapPrioridad(data.get('id'),data.get('password'))
        pos = hash.hashFunction()
        hash.insert(pos,user)
    def InsertDato2(self, hash, data):
        user = mapPrioridad(data.id,data.password)
        pos = hash.hashFunction()
        hash.insert(pos,user)
    #ESTA FUNCIÓN ELIMINA UN DATO DE LA ESTRUCTURA
    def EliminarDato(self, arbol,posicion,lista):
        arbol.eliminarNodo(posicion)

    def BuscarDato(self,hash, user):
        if hash.hasKey(user):
            return hash.getKey(user)
        return False

    #ESTA FUNCIÓN CONSULTA TODOS LOS DATOS DE LA ESTRUCTURA
    def ConsultaTodo(self,arbol):
        for i in range(arbol.retornarTamano()):
            print(arbol.devolverData(i))
    def AgregarDatosHash(self, lista,candtidaddatos):
        #nodo=Node(lista[0].get('id'),lista[0])
        #arbol = AVLtree(nodo)
        hash=HashTable(11)
        i=0
        CANTIDAD_DATOS=candtidaddatos
        while(i<CANTIDAD_DATOS):
            user = mapPrioridad(lista[i].get('id'),lista[i].get('password'))
            pos = hash.hashFunction()
            hash.insert(2,user)
            i+=1
        return hash
    def Ingreso(self, arbol, user):
        for i in range(arbol.retornarTamano()):
            if(user==arbol.devolverData(i)):
                return True
        return False 

