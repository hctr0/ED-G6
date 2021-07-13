class Node():

    def __init__(self, key, right = None, left = None, parent = None, height = 1):
        self.key = key
        self.right = right
        self.left = left
        self.parent = parent
        self.height = height




class AVLtree():
    def getHeight(self, root):
        if root == None:
            return 0
        
        return root.height

    
    def Rotateleft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))


    def Rotateright(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.righy))

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y


    def search(self, key, root):
        if key == root.key:
            return root
        elif key < root.key:
            if root.left != None: 
                self.search(key, root.left)
            else:
                return root
        elif key>root.key:
            if root.left != None:
                self.search(key, root.right)
            else:
                return root


    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
    def Rebalance(N):
        P = N.parent
        if N.left.height > N.right.height+1:
                return





def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.key)
        printTree(node.right, level + 1)



