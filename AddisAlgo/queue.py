class queueClass:
    def __init__(self, size):
        self.size = size
        self.source = [0 for i in range(self.size)] 
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return True if self.front == -1 else  False 

    def isFull(self):
        return True if ((self.front - self.rear > 0) or (self.rear - self.front == len(self.source) -1)) else  False 

    def dequeue(self):
        if self.isEmpty() != True:
            self.front += 1
            return self.source[self.front - 1]
        else:
            print("The Queue is empty, No more vlaues to dequeue", "\n")
            return None

    def enqueue(self, value):
        if self.isFull() != True:
            if self.isEmpty() == True:
                self.front += 1
            self.rear += 1
            self.source[self.rear] = value
            return True
        else:
            print("The Queue is full, cannot enqueue anymore values", "\n")
            return None

    