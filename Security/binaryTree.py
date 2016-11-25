from queue import Queue
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
class BinaryTree:
    def __init__(self):
        self.head = None
        self.counter = 0
        self.rec = ""
    def printTreeRec(self, curr):
        if curr.left != None:
            self.printTreeRec(curr.left)
        print(curr.data)
        if curr.right != None:
            self.printTreeRec(curr.right)
    def printTree(self):
        self.printTreeRec(self.head)
    def add(self, value):
        q = Queue()
        if self.head != None:
            q.push(self.head)
            while True:
                temp = q.pop()
                if temp.left == None:
                    newNode = Node()
                    newNode.data = value
                    temp.left = newNode
                    break
                elif temp.right == None:
                    newNode = Node()
                    newNode.data = value
                    temp.right = newNode
                    break
                else:
                    q.push(temp.left)
                    q.push(temp.right)
        else:
            newNode = Node()
            self.head = newNode
            self.head.data = value
        self.counter += 1
    def getRec(self, curr):
        if curr.left != None:
            self.getRec(curr.left)
        self.rec = self.rec + curr.data
        if curr.right != None:
            self.getRec(curr.right)
    def get(self):
        self.getRec(self.head)
        return self.rec