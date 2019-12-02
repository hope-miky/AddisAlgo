class search:
    def __init__(self):
        self.val = []
        self.last = 0
        self.first = 0
        self.mid = 0
        self.temp = 0


    def Linear(self, value, source):
        for i in range(len(source)):
            if source[i] == value:
                self.val.append(i)
        
        return self.val

        
    def Binary(self, value, source):
        self.last = len(source) - 1
        self.mid = self.midFinder(self.first, self.last)
        while value != source[self.mid]:
            if value > source[self.mid]:
                self.first = self.mid + 1
                self.mid = self.midFinder(self.first, self.last)
            elif value < source[self.mid]:
                self.last = self.mid -1
                self.mid = self.midFinder(self.first, self.last)
            if self.first == self.mid:
                print("Item not found")
                return None

        return self.mid
    def midFinder(self, f, l):
        return self.first + (l-f)/2
         