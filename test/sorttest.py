import sys
sys.path.append('~/Documents/GitHub/AddisAlgo/')

from AddisAlgo.sort import sort

class simpleSortClass:
    def __init__(self):
        self.sort = sort()
        pass

    def bubbleSort(self):
        #print(self.search.Linear(value=1, source=[1,5,4,7,8,1,9,8,7,2,3,7]))
        print(self.sort.bubble(source=[1,5,4,7,8,1,9,8,7,2,3,7]))
    
if __name__ == '__main__':
    obj = simpleSortClass()
    obj.bubbleSort()