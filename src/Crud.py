from resources.Nodo import *
from resources.ListNodes import * 
from mysqlconnections import *

class Crud:
    #ESTA FUNCION ACTUALIZA UN DATO EN LA ESTRUCTURA
    def ActualizarDato(self, listaNodos, posicion, value,lista):
        listaNodos.editarNodo(posicion, value)
        database = DataBase()
        database.update_date(value, lista[posicion][0])
        database.close_connection()
    #FUNCION DISEÑADA PARA INSERTAR UN DATO


    def InsertDato(self, listaNodos, data):
        listaNodos.agregarNodo(data)
        database = DataBase()
        database.insert_data(data)
        database.close_connection()
    #ESTA FUNCIÓN ELIMINA UN DATO DE LA ESTRUCTURA
    def EliminarDato(self, listaNodos,posicion,lista):
        listaNodos.eliminarNodo(posicion)
        database = DataBase()
        database.delete_date(lista[posicion][0])
        database.close_connection()

    #ESTA FUNCIÓN BUSCA UN DATO EN LA ESTRUCTURA


    def BuscarDato(self,listaNodos,posicion):
        return listaNodos.devolverData(posicion)

    #ESTA FUNCIÓN CONSULTA TODOS LOS DATOS DE LA ESTRUCTURA
    def ConsultaTodo(self,listaNodos):
        for i in range(listaNodos.retornarTamano()):
            print(listaNodos.devolverData(i))
    def Ingreso(self, listaNodos, user):
        for i in range(listaNodos.retornarTamano()):
            if(user==listaNodos.devolverData(i)):
                return True
        return False    


