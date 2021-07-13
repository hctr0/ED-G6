class Node():

    def __init__(self, key, right = None, left = None, parent = None, height = 1):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent
        self.height = height



class BinaryTree():

    def __init__(self, key = None):
        aux = Node(key)
        if key != None:
            self.root = aux

    def search(self, k):
        aux = self.root

        while aux:
            if aux.key == k:
                return aux

            elif aux.key>k:
                if aux.left != None:
                    aux = aux.left
                else:
                    return aux

            elif aux.key<k:
                if aux.right != None:
                    aux = aux.right
                else:
                    return aux



    def insert(self, k):
        aux = search(k)
        if aux.key>k:
            aux.left = Node(k, parent=aux)
        else:
            aux.right = Node(k, parent=aux)





class AVLtree():

    def __init__(self, nodo = None):
        self.nodo = nodo

    def search(self, key, R):
        return

    def insert(self, key, R):
        return
    def Rebalance(N):
        P = N.parent
        if N.left.height > N.right.height+1:
                return

    def delete(self, value, R):
        return
