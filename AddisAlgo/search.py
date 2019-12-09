'''
Searching Algorithms for AdisAlgo 
The class consists of 
                    - Linear Search
                    - Binary Search 
'''
class search:
    def __init__(self):
        self.val = [] #return array for liner search 
        self.last = 0
        self.first = 0
        self.mid = 0
        self.temp = 0    # temporary value storage

    #Linear search method
    def Linear(self, value, source):
        for i in range(len(source)):
            if source[i] == value:
                self.val.append(i)
        
        return self.val

    #Binary search method
    def Binary(self, value, source):
        self.last = len(source) - 1
        self.mid = self.midFinder(self.first, self.last)
        
        while value != source[self.mid]:
            # If the first is equal to middle the item is not found so return none 
            if self.first == self.mid:
                print("Item not found")
                return None
            # when the item is greater than the middle value
            if value > source[self.mid]:
                self.first = self.mid + 1
                self.mid = self.midFinder(self.first, self.last)
            # when the item is less than the middle item 
            elif value < source[self.mid]:
                self.last = self.mid -1
                self.mid = self.midFinder(self.first, self.last)
                
        return self.mid     # return the item 

    # New middle finder 
    def midFinder(self, f, l):
        return int(self.first + (l-f)/2)
         