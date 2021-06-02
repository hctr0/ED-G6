from resources.Cola import *
from resources.ListNodes import * 
from mysqlconnections import *

class CrudF:
    '''def InsertDato(self, pila, data):
        pila.apilar(data)
        database = DataBase()
        database.insert_data(data)
        database.close_connection()
    def AgregarDatosListas(self, lista):
        pila1 = Pila() 
        pila1.apilar(lista[0][1])
        i=1
        while(i<100000):
            pila1.apilar(lista[i][1])         
            i+=1
        return pila1
    def EliminarDato(self, pila,lista):
        pila.desapilar()
        database = DataBase()
        database.delete_date(len(lista))
        database.close_connection()
    def ConsultaTodo(self,pila):
        pila.imprimir()'''
    def InsertDato(self, cola, data):
        cola.enqueue(data)
        database = DataBase()
        database.insert_data(data)
        database.close_connection()
    def AgregarDatosListas(self, lista):
        cola1 = Queue() 
        cola1.enqueue(lista[0][1])
        i=1
        while(i<100000):
            cola1.enqueue(lista[i][1])         
            i+=1
        return cola1
    def EliminarDato(self, cola,lista):
        cola.dequeue()
        database = DataBase()
        database.delete_date(lista[0][0])
        database.close_connection()
    def ConsultaTodo(self,cola):
        cola.print_all()