import sys
sys.path.append('~/Documents/GitHub/AddisAlgo/')

from samples import stack

class simpleTestClass:
    def __init__(self):
        pass

    def testStack(self):
        self.stack = stack.stackClass(7)
        print(self.stack.isFull())
        print(self.stack.source, ' ', self.stack.isEmpty())

        self.stack.push(1)

        self.stack.push(2)

        self.stack.push(3)

        self.stack.push(4)

        print(self.stack.source, ' ', self.stack.isEmpty())




if __name__ == '__main__':
    obj = simpleTestClass()
    obj.testStack()