from Crud import *
if __name__ == "__main__":
    funciones =Crud()
    database=DataBase()
    lista = database.select_all_user()
    database.close_connection()
    listaNodos = ListNodes(lista[0][1])
    i=1
    while(i<len(lista)):
        listaNodos.agregarNodo(lista[i][1])         
        i+=1
    nombre =input() 
    A =funciones.Ingreso(listaNodos,nombre)
    if(A):
        print("ha ingresado")
    else:
        print("Usuario incorrecto")
        exit()
    
    #funciones.ActualizarDato(listaNodos, 4,"gio",lista)
    
    #funciones.InsertDato(listaNodos, "jjj")
    #listaNodos.retornarUltimoNodo()
    #print(funciones.BuscarDato(listaNodos, 0))
    #funciones.ConsultaTodo(listaNodos)