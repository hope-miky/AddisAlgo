class stack:
    def __init__(self):
        self.sourse = []
        self.top = -1

    def ceckEmpty(self):
        return self.top
    
    def pop(self):
        self.top -= 1
        return top

    def push(self, value):
        self.top += 1
        self.sourse[top] = value

    