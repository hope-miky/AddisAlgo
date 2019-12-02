import sys
sys.path.append('~/Documents/GitHub/AddisAlgo/')

from AddisAlgo import search

class simpleTestClass:
    def __init__(self):
        pass

    def linearSearch(self):
        self.search = search()
        print(search.search(value=1, source=[2,5,4,7,8,1,9,8,7,2,3,7], type="linear"))
    
if __name__ == '__main__':
    obj = simpleTestClass()
    obj.linearSearch()