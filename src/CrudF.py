
from src.resources.ListNodes import *
from src.resources.ColaPrioridad import *
from src.resources.mapPrioridad import *

class CrudF:
    def crearColaPrioridad(self,lista):
        cola = PriorityQueue()
        for i in range(len(lista)):
            prioridad=CrudF.crearLLave(lista[i])
            valor=lista[i]
            solicitud=mapPrioridad(prioridad,valor)
            cola.insert(solicitud)
        return cola
    def crearLLave(solicitud):
       prioridad=0
       if solicitud.solicitud.lower() == "traslado":
           prioridad+=50
       if solicitud.solicitud.lower() == "cambio de grupo":
           prioridad+=7
       if solicitud.solicitud.lower() == "inscripcion":
           prioridad+=7
       if solicitud.solicitud.lower() == "carga":
           prioridad+=8
       if solicitud.solicitud.lower() == "inscripcion":
           prioridad+=6
       if solicitud.solicitud.lower() == "cancelaciona":
           prioridad+=6
       if solicitud.solicitud.lower() == "reserva":
           prioridad+=9
       if solicitud.solicitud.lower() == "cancelacionp":
           prioridad+=10
       if solicitud.solicitud.lower() == "cambiot":
           prioridad+=12
       if solicitud.solicitud.lower() == "reembolso":
           prioridad+=16
       prioridad+=solicitud.id
       return prioridad
    def devolverLista(self, mapPrioridad):
        lista=[]
        while not mapPrioridad.isEmpty():
            lista.append(mapPrioridad.delete().value)
        return lista
        


