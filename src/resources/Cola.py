#CREACIÓN DE UN NODO, PROBABLEMENTE PUEDA GENERARSE UNA CLASE NODO ÚNICA MÁS ADELANTE

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


# CREACIÓN DE CLASE COLA (FIFO)

class Queue:
    
    #LA COLA DEBE INICIAR VACÍA, DECLARANDOSE ANTES DE SU USO SIN NINGÚN PARAMETRO
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
    
    
    #LA FUNCIÓN enqueue AGREGA UN VALOR AL FINAL DE LA COLA, REQUIERE UN VALOR
    def enqueue(self, value):
        aux = Node(value)
        if(self.head.value == None):
            self.head = aux
            self.tail = aux
        else:
            self.tail.next = aux
            self.tail = aux
    
    #LA FUNCIÓN dequeue REGRESA EL PRIMER VALOR DE LA COLA, SACANDOLO DE ESTA.
    def dequeue(self):
        aux = self.head
        self.head = self.head.next
        return aux

    #LA FUNCIÓN is_empty REGRESA UN BOOLEANO, TRUE SI ESTÁ VACÍA, FALSE SI TIENE ALGUN ELEMENTO 
    def is_empty(self):
        if(self.head.value == None):
            return True
        else:
            return False
    
    #FUNCIÓN EXTRA QUE PERMITE IMPRIMIR TODOS LOS VALORES DE LA COLA SEGUIDOS DE UN SALTO DE LINEA
    def print_all(self):
        aux = self.head
        if(aux.value!=None):
            while(aux!= None):
                print(aux.value)
                aux = aux.next
        else:
            print("Empty")
