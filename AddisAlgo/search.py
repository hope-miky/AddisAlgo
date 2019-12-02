class search:
    def __init__(self, value, source, type):
        self.value = value
        self.source = source
        self.type = type

        if self.type == "linear":
            self.linearSearch()

    def linearSearch(self):
        for i in range(len(self.source)):
            if self.source[i] == self.value:
                return i
        
        return None 