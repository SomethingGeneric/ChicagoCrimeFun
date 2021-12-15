class SomeData:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __lt__(self, other):
        if self.key < other.key:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.key > other.key:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False
    def strval(self):
        return str(self.val)
    def __str__(self):
        return "\"Key: " + str(self.key) + ", Val: " + str(self.val) + "\""
    def __repr__(self):
        return "\"Key: " + str(self.key) + ", Val: " + str(self.val) + "\""


class SomeHeap:
    def __init__(self):
        self.data = []
        self.size = 0
    def insert(self, some, thing):
        self.data.append(SomeData(some,thing))
        self.data.sort()
        self.size += 1
    def remove(self):
        if not self.is_empty():
            print("Size is " + str(self.size))
            dat = self.data.pop(0)
            k,v = dat.key, dat.val
            self.size -= 1
            return (k,v)
        else:
            return (None, None)
    def peek(self):
        if not self.is_empty():
            dat = self.data[0]
            k,v = dat.key, dat.val
            return (k,v)
        else:
            return (None, None)
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
    def valrepr(self):
        foo = ""
        for x in self.data:
            foo += x.strval() + "\n"
        return foo

if __name__ == "__main__":
    h = SomeHeap()
    h.insert(2,"lolxd")
    h.insert(1,"haha")
    h.insert(3,"this_is_funny")
    h.insert(0, "first!")
    print(str(h))
    print(str(h.peek()))
    print(str(h.remove()))
    print(str(h.peek()))
    print(str(h))
