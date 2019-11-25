class stackClass:
    def __init__(self, size):
        self.size = size
        self.source = [0 for i in range(self.size)] 
        self.top = -1

    def isEmpty(self):
        return True if self.top == -1 else  False 

    def isFull(self):
        return True if self.top == self.size else  False 

    def pop(self):
        if !isEmppty()
        self.top -= 1
        return top

    def push(self, value):
        self.top += 1
        self.source[self.top] = value

    