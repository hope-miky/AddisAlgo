# AddisAlgo
AddisAlgo is python library to implement various algorithms and datastructures. The code is pure python and designed to use minimum memory and space. Algoeithms and data structures consisted in version 1.0 are:

* Stack
* Queue
* Linear Search 
* Binary Search
* Bubble Sort
  
## Stack
The stack class will help implement the stack datatructure in user friendly way. The class consists 4 methods. In order to use the stack method we can import it  like this.
```python
from AddisAlgo import stack
```
#### Push
```python
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
```python
        stack = stack.stackClass(7)
        stack.push(1)
```
#### Pop
```python
def pop(self):
        if self.isEmpty() != True:
            self.top -= 1
            return self.source[self.top + 1]
        else:
            print("The stack is empty, No more vlaues to pop", "\n")
            return None
```
The pop method checks if the stack/array is empty and if not it will pop a value from the array, return that value and update the top index. In order to use it we can use something like this:
```
        stack.pop()
```