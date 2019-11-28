class stackClass:
    def __init__(self, size):
        self.size = size
        self.source = [0 for i in range(self.size)] 
        self.top = -1

    def isEmpty(self):
        return True if self.top == -1 else  False 

    def isFull(self):
        return True if self.top == self.size -1 else  False 

    def pop(self):
        if self.isEmpty() != True:
            self.top -= 1
            return self.source[self.top + 1]
        else:
            print("The stack is empty, No more vlaues to pop", "\n")
            return None

    def push(self, value):
        if self.isFull() != True:
            self.top += 1
            self.source[self.top] = value
            return True
        else:
            print("The stack is full, cannot accept anymore values", "\n")
            return None

    