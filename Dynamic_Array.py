import ctypes


class My_list:
    def __init__(self) -> None:
        self.n = 0
        self.size = 1
        self.arr = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        self.arr[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        arr_new = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            arr_new[i] = self.arr[i]
        self.arr = arr_new

    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()

    def __str__(self) -> str:
        result = ''
        for i in range(self.n):
            result = result + str(self.arr[i])+","

        return f"[{result[:-1]}]"

    def __getitem__(self, index):
        try:
            print(self.arr[index])
        except IndexError:
            return "Index error - index out of bound"

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size*2)

        self.arr[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return 'empty list'
        self.n = self.n-1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, value):
        for i in range(self.n):
            if self.arr[i] == value:
                return i
        return -1

    def insert(self, index, value):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n-1, index-1, -1):
            self.arr[i + 1] = self.arr[i]

        self.arr[index] = value
        self.n += 1

    def delete(self, index):
        if index <= self.n:
            for i in range(index, self.n-1):
                self.arr[i] = self.arr[i+1]

            self.n -= 1
        return "index does to exist"

    def remove(self, value):
        index = self.find(value)
        if not index == -1:
            self.delete(index)
        return "Value Not found"


l = My_list()
l.append(5)
l.append("h")
l.append("k")
l.append("56")
l.append(20)

# l.pop()
# print(l)
# l.clear()

# print(l)
# l.insert(6, "insert")
# print(l)

print(l)
