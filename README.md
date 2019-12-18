# AddisAlgo
AddisAlgo is python library to implement various algorithms and datastructures. The code is pure python and designed to use minimum memory and space. Algoeithms and data structures consisted in version 1.0 are:

* Stack
* Queue
* Linear Search 
* Binary Search
* Bubble Sort
  
## Stack
The stack class will help implement the stack datatructure in user friendly way. The class consists 4 methods. In order to use the stack method we can import it  like this.
```
from AddisAlgo import stack
```
#### Push
```
def push(self, value):
        if self.isFull() != True:
            self.top += 1
            self.source[self.top] = value
            return True
        else:
            print("The stack is full, cannot accept anymore values", "\n")
            return None

```
The push method checks if the stack/array is full and if not it will push the value to the array and update the top index. In order to use it we can use something like this by spacifing the length of the stack, which is in our case 7:
```
        stack = stack.stackClass(7)
        self.stack.push(1)
        self.stack.pop()
```

