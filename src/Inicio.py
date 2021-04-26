from Crud import *
import os 

clearlnx = lambda: os.system('clear')
clearwin = lambda: os.system('cls')


def menu_principal():
    clearlnx()
    clearwin()
    print(" Bienvenido al sistema ")
    print("Por favor seleccione una de las siguientes opciones: ")
    print("1. Editar usuarios")
    print("2. Solicitudes")
    print("3. Terminar proceso\n")
    opt = input()
    
    return opt


def menu_usuario(funciones, listaNodos, lista):
    clearlnx()
    clearwin()
    print("Usuarios")
    print("1. Agregar Usuario")
    print("2. Borrar Usuario")
    print("3. Mostrar todos los usuarios")
    print("4. Regresar")
    opt = input()
    
    if (opt == "1"):
        nuevouser = input("Ingrese el nombre de usuario: ")
        funciones.InsertDato(listaNodos, nuevouser, lista)
        print("Agregando usuario")
        print("Presione enter para continuar")
        input()

    elif (opt == "2"):
        pos = int(input("Seleccione la posición: "))
        funciones.Eliminando(listaNodos, pos, lista )
        print("Eliminando usuario")
        print("Presione enter para continuar")
        input()

    elif (opt == "3"):
        print("Imprimiendo todos los usuarios")
        funciones.ConsultaTodo(listaNodos)
        print("Todos los usuarios impresos")
        print("Presione enter para continuar")
        input()

    elif (opt == "4"):
        return opt
    else:
        print("Opción no válida")
        print("Volviendo al menú principal")    
        input()


def menu_solicitudes(funciones, listaNodos, lista):
    clearlnx()
    clearwin()
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
        return opt    
    else:
        print("Opción no válida")
        print("Volviendo al menú principal")    
        input()




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