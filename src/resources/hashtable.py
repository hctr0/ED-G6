import random
import src.resources.mapPrioridad
class HashTable():
    def __init__(self):
        self.map=[None]*11
        self.a=2
        self.n=0
        self.loadFactor=int(self.n/len(self.map))
    def hashFunction(self):
        k=random.randint(0,len(self.map))
        hashPos = (self.a*k)%len(self.map)
        return hashPos
    def insert(self, pos, map):
        chain =[]
        chain.append(map)
        self.map[pos]=chain
    def getKey(self, llave):
        for map in self.map:
            for value in map:
                if value.prioridad==llave:
                    return value.value
    def hasKey(self, llave):
        for map in self.map:
            for value in map:
                if value.prioridad==llave:
                    return True
        return False
