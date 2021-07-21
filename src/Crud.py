from src.resources.ListNodes import *
from src.resources.Arbolavl import *
from .models import User
class Crud:
    #ESTA FUNCION ACTUALIZA UN DATO EN LA ESTRUCTURA
    def ActualizarDato(self, arbol, value):
        arbol.search(arbol.root, value)
    #FUNCION DISEÑADA PARA INSERTAR UN DATO
    def InsertDato(self, arbol, data):
        arbol.insert(arbol.root,data.id,data)
    #ESTA FUNCIÓN ELIMINA UN DATO DE LA ESTRUCTURA
    def EliminarDato(self, arbol,posicion,lista):
        arbol.eliminarNodo(posicion)

    #ESTA FUNCIÓN BUSCA UN DATO EN LA ESTRUCTURA
    def ExisteDato_boolean(self,arbol, user):
        try:
            arbol.search(arbol.root, user)
            return True
        except:
            return False
            
    def BuscarDato(self,arbol, user):
        return arbol.search(arbol.root,user)

    #ESTA FUNCIÓN CONSULTA TODOS LOS DATOS DE LA ESTRUCTURA
    def ConsultaTodo(self,arbol):
        for i in range(arbol.retornarTamano()):
            print(arbol.devolverData(i))
    def AgregarDatosArbol(self, lista,candtidaddatos):
        nodo=Node(lista[0].get('id'),lista[0])
        arbol = AVLtree(nodo)
        i=1
        CANTIDAD_DATOS=candtidaddatos
        while(i<CANTIDAD_DATOS):
            arbol.insert(arbol.root,lista[i].get('id'),lista[i])
            i+=1
        return arbol
    def Ingreso(self, arbol, user):
        for i in range(arbol.retornarTamano()):
            if(user==arbol.devolverData(i)):
                return True
        return False 

