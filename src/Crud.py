from src.resources.ListNodes import *
from .models import User
class Crud:
    #ESTA FUNCION ACTUALIZA UN DATO EN LA ESTRUCTURA
    def ActualizarDato(self, listaNodos, posicion, value,lista):
        listaNodos.editarNodo(posicion, value)
    #FUNCION DISEÑADA PARA INSERTAR UN DATO
    def InsertDato(self, listaNodos, data):
        listaNodos.agregarNodo(data)
    #ESTA FUNCIÓN ELIMINA UN DATO DE LA ESTRUCTURA
    def EliminarDato(self, listaNodos,posicion,lista):
        listaNodos.eliminarNodo(posicion)

    #ESTA FUNCIÓN BUSCA UN DATO EN LA ESTRUCTURA
    def ExisteDato_boolean(self,listaNodos, user):
        for i in range(listaNodos.retornarTamano()):
            if(listaNodos.devolverData(i).get('user')==user):
                return True
        return False
    def BuscarDato(self,listaNodos, user):
        #print(user, )
        for i in range(listaNodos.retornarTamano()):
            print(listaNodos.devolverData(i).get('user'), "  -- ", user)
            if(listaNodos.devolverData(i).get('user')==user):
                user1 = User(listaNodos.devolverData(i).get('user'),listaNodos.devolverData(i).get('password'))
                return user1
        print('No existe el usuario')

    #ESTA FUNCIÓN CONSULTA TODOS LOS DATOS DE LA ESTRUCTURA
    def ConsultaTodo(self,listaNodos):
        for i in range(listaNodos.retornarTamano()):
            print(listaNodos.devolverData(i))
    def AgregarDatosListas(self, lista):
        listaNodos = ListNodes(lista[0])
        i=1
        while(i<1000):
            listaNodos.agregarNodo(lista[i])         
            i+=1
        return listaNodos
    def Ingreso(self, listaNodos, user):
        for i in range(listaNodos.retornarTamano()):
            if(user==listaNodos.devolverData(i)):
                return True
        return False   
    def OrdenarListaAlfabeticamente(self,lista):
        listaNueva=[]
        i=1
        while(i<1000):
            listaNueva.append(str(lista[i][1]))         
            i+=1
        listaNueva.sort()
        listaNodos = ListNodes(listaNueva[0])
        i2=1
        while(i2<len(listaNueva)):
            listaNodos.agregarNodo(listaNueva[i2])         
            i2+=1
        return listaNodos

