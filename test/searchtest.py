import sys
sys.path.append('~/Documents/GitHub/AddisAlgo/')

from AddisAlgo.search import search

class simpleTestClass:
    def __init__(self):
        self.search = search()
        pass

    def linearSearch(self):
        #print(self.search.Linear(value=1, source=[1,5,4,7,8,1,9,8,7,2,3,7]))
        print(self.search.Binary(value=8, source=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    
if __name__ == '__main__':
    obj = simpleTestClass()
    obj.linearSearch()