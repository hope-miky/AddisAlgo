import ctypes

class Array:
    def __init__(self, size):
        assert size>0, 'Array size must be greater than 0'
        self._size = size
        self.curindex = 0
        self.ctypearray = ctypes.py_object * self._size
        self.values = self.ctypearray()
        for i in range(self._size):
            self.values[i] = None
        print(self.values)


    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        assert index >= 0 and index < len(self), 'Array index is out of range'
        return self.values[index]
    
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), 'Array index is out of range'
        self.values[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.curindex < self._size:
            val = self.values[self.curindex]
            self.curindex += 1
            return val
        else:
            self.curindex = 0
            raise StopIteration 

    def __add__(self, other):
        for i in range(self._size):
            self.values[i] = self.values[i] + other
        return self.values

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        for i in range(self._size):
            self.values[i] = self.values[i] - other
        return self.values

    def __rsub__(self, other):
        for i in range(self._size):
            self.values[i] = other - self.values[i]
        return self.values

    def __mul__(self, other):
        for i in range(self._size):
            self.values[i] = self.values[i] * other
        return self.values

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        for i in range(self._size):
            self.values[i] = self.values[i] / other
        return self.values

    def __rdiv__(self, other):
        for i in range(self._size):
            self.values[i] = other / self.values[i] 
        return self.values

    def __mod__(self, other):
        for i in range(self._size):
            self.values[i] = self.values[i] % other
        return self.values

    def __rmod__(self, other):
        for i in range(self._size):
            self.values[i] = other % self.values[i]
        return self.values

    # Type Convetion methods 

if __name__ == '__main__':
    ar = Array(6)
    ar[0] = 0
    ar[1] = 1
    ar[2] = 2
    ar[3] = 3
    ar[4] = 4
    ar[5] = 5
    for i in ar:
        print(i)
    2 + ar

    for i in ar:
        print(i)