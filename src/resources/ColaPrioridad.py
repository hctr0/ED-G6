from src.resources.ListNodes import *
class ColaPrioridad(object):
    def __init__(self):
        self.queue = None

    def isEmpty(self):
        return self.queue.retornarTamano() == 0

    def insert(self, data):
        if(self.queue==None):
            self.queue=ListNodes(data)
            return
        self.queue.agregarNodo(data)
    def delete(self):
        try:
            min = 0
            for i in range(self.queue.retornarTamano()):
                if self.queue.devolverData(i).prioridad < self.queue.devolverData(min).prioridad:
                    min = i
            item = self.queue.devolverData(min)
            self.queue.eliminarNodo(min)
            return item
        except IndexError:
            print()
            exit()
