class Node:
    def __init__(self):
        self.data = ""
        self.childs = []

class Tree:
    def __init__(self):
        self.temp = 0
        #self.node = Node()
        self.root = Node()
    
    def addChild(self, node):
        node.childs.push(node)

    def printTree(self, root):
        print(root.data)
        while root:
            for i in root.childs:
                print(i.data)
                if len(i.childs) > 0:
                    slef.printTree(i)


if __name__ == '__main__':
    
        


