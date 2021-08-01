import random
class HashTable():
    def __init__(self, size):
        self.map=[None]*size
        self.n=0
    def hashFunction(self):
        k=random.randint(0,len(self.map)-1)
        hashPos = (2*k)%len(self.map)
        return hashPos
    def loadFactor(self):
        return int(self.n/len(self.map))

    def insert(self, pos, map):
        if self.map[pos]==None:
            self.map[pos]=[]
        self.map[pos].append(map)
        self.n+=1

        self.rehasing()
    def getKey(self, llave):
        for map in self.map:
            if map!=None:
                for value in map:
                    if value.prioridad==llave:
                        return value.value
    def rehasing(self):
        if self.loadFactor()>0.9:
            """ print(self.n, 'numero de items')
            print(len(self.map), 'm-cardinalidad')
            print(self.loadFactor()) """
            i=0
            newhash=HashTable(len(self.map)*2+1)
            for map in self.map:
                if map!=None:
                    for value in map:
                        pos= newhash.hashFunction()
                        newhash.insert(pos,value)
            self.map = newhash.map
            self.n=newhash.n
            print(len(self.map), 'map Nuevo')
            return
    def hasKey(self, llave):
        for map in self.map:
            if map!=None:
                for value in map:
                    if value.prioridad==llave:
                        return True
        return False
