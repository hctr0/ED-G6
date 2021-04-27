from Crud import *
from time import time
import os 

clearlnx = lambda: os.system('clear')
clearwin = lambda: os.system('cls')


def menu_principal():
    clearlnx()
    print(" Bienvenido al sistema ")
    print("Por favor seleccione una de las siguientes opciones: ")
    print("1. Editar usuarios")
    print("2. Solicitudes")
    print("3. Terminar proceso\n")
    opt = input()
    
    return opt


def menu_usuario(funciones, listaNodos, lista):
    clearlnx()
    print("Usuarios")
    print("1. Agregar Usuario")
    print("2. Borrar Usuario")
    print("3. Mostrar todos los usuarios")
    print("4. Ordenar lista ALfabeticamente")
    print("5. Actualizar dato")
    print("6. Recibir un dato")
    print("7. Regresar")
    opt = input()
    
    if (opt == "1"):
        nuevouser = input("Ingrese el nombre de usuario: ")
        startTime = time()
        funciones.InsertDato(listaNodos, nuevouser)
        lastTime = time() -startTime
        print(lastTime)
        print("Agregando usuario")
        print("Presione enter para continuar")
        input()

    elif (opt == "2"):
        pos = int(input("Seleccione la posición: "))
        userName = funciones.BuscarDato(listaNodos, pos)
        startTime = time()
        funciones.EliminarDato(listaNodos, pos, lista )
        lastTime = time() -startTime
        print(lastTime)
        print("Eliminado usuario " + userName  )
        print("Presione enter para continuar")
        input()

    elif (opt == "3"):
        print("Imprimiendo todos los usuarios")
        startTime = time()
        funciones.ConsultaTodo(listaNodos)
        lastTime = time() -startTime
        print(lastTime)
        print("Todos los usuarios impresos")
        print("Presione enter para continuar")
        input()

    elif (opt == "4"):
        print("Organizando los datos")
        startTime = time()
        listaNodos = funciones.OrdenarListaAlfabeticamente(lista)
        lastTime = time() -startTime
        funciones.ConsultaTodo(listaNodos)
        print(lastTime)
        print("Datos organizados")
        print("Presione enter para continuar")
        input()
    elif (opt == "5"):
        print("Actualizar dato")
        print("Digite la posicion que desea editar")
        posicion = int(input())
        print("Digite el nuevo nombre")
        value = input()
        startTime = time()
        funciones.ActualizarDato(listaNodos, posicion, value, lista)
        lastTime = time() -startTime
        print(lastTime)
        print("Datos actualizado")
        print("Presione enter para continuar")
        input()
    elif (opt == "6"):
        print("Retornar dato")
        print("Digite la posicion del dato que desea recibir")
        posicion = int(input())
        startTime = time()
        print("El dato en la posisicio {} es ".format(posicion) +funciones.BuscarDato(listaNodos, posicion))
        lastTime = time() -startTime
        print(lastTime)
        print("Datos actualizado")
        print("Presione enter para continuar")
        input()
    else:
        print("Opción no válida")
        print("Volviendo al menú principal")    
        input()


def menu_solicitudes(funciones, listaNodos, lista):
    clearlnx()
    print("Solicitudes")
    print("1. Elegir solicitud")
    print("2. Cambiar estado de solicitud")
    print("3. Regresar")
    opt = input()
    if (opt == "1"):
        print("Eligiendo solicitud")
        print("Presione enter para continuar")
        input()

    elif (opt=="2"):
        print("Cambiando estado de solicitud")
        print("Presione enter para continuar")
        input()

    elif (opt == "3"):
        return exit()    
    else:
        print("Opción no válida")
        print("Volviendo al menú principal")    
        input()

def traerDatoInicio():
    return 801;



if __name__ == "__main__":
    funciones =Crud()
    database=DataBase()
    lista = database.select_all_user()
    database.close_connection()
    startTime = time()
    listaNodos = funciones.AgregarDatosListas(lista)
    lastTime = time() -startTime
    print(lastTime)
         
    print("Ingrese su nombre de usuario")
    nombre =input() 
    State = funciones.Ingreso(listaNodos,nombre)

    if(State == True):
        print("Ingreso correcto")
        print("Presione enter para continuar")
    else:
        print("Usuario incorrecto")
        exit()
    #MENU PRINCIPAL QUE TOMA LAS FUNCIONES ARRIBA
    while True:
        opt = menu_principal()
        if (opt=="1"):
            a = menu_usuario(funciones, listaNodos, lista)
            if (a == "3"):
                pass
        elif(opt=="2"):
            a = menu_solicitudes(funciones, listaNodos, lista)
            if (a =="4"):
                pass

        elif(opt == "3"):
            print("Terminando procesos")
            exit()
        else:
            print("Opción no valida")
            print("Presione enter para volver al menú inicial")
            input()

    #funciones.ActualizarDato(listaNodos, 4,"gio",lista)
    
    #funciones.InsertDato(listaNodos, "jjj")
    #listaNodos.retornarUltimoNodo()
    #print(funciones.BuscarDato(listaNodos, 0))
    #funciones.ConsultaTodo(listaNodos)