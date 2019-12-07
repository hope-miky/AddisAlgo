class sort:
    def __init__(self):
        self.temp = 0 

    def bubble(self, source):
        for i in range(1, len(source) - 1):
            for j in range(len(source) - i):
                if source[j] > source[j+1]:
                    self.temp = source[j]
                    source[j] = source[j+1]
                    source[j+1] = self.temp
        return source
            
    