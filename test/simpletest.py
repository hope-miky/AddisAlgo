import sys
sys.path.append('~/Documents/GitHub/AddisAlgo/')

from AddisAlgo import stack, queue

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

        self.stack.push(5)

        self.stack.push(6)

        self.stack.push(7)

        self.stack.push(8)

        self.stack.pop()

        self.stack.pop()

        self.stack.pop()

        self.stack.push(7)

        self.stack.push(6)

        self.stack.push(5)

        print(self.stack.source, ' ', self.stack.isEmpty())
    

    def testQueue(self):
        self.queue = queue.queueClass(7)

        print(self.queue.isFull())

        print(self.queue.isEmpty())

        print("sourse array = ", self.queue.source, "\n")
        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")

        self.queue.enqueue(1)

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")
        
        self.queue.enqueue(2)

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")

        self.queue.enqueue(3)

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")

        self.queue.enqueue(4)

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")

        self.queue.enqueue(5)

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")

        self.queue.dequeue()

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")


        self.queue.dequeue()

        print("front = {}, rear = {} ".format(self.queue.front, self.queue.rear), "\n")
        print("sourse array = ",self.queue.source, "\n")


if __name__ == '__main__':
    obj = simpleTestClass()
    obj.testQueue()