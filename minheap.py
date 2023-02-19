import sys

class MinHeap:
    def __init__(self, maxsize=100000):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [(0, 0)] * (self.maxsize + 1)
        self.heap[0] = (-1 * sys.maxsize, -1 * sys.maxsize)
        self.FRONT = 1

    def is_leaf(self, i):
        return True if i > (self.size // 2) and i <= self.size else False

    def insert(self, priority, dispatch_string):
        if priority is None:
            priority = float('inf')
        if dispatch_string is None:
            dispatch_string = ""
        element = (priority, dispatch_string)
        self.heap.append(element)
        self.size += 1
        current = self.size - 1
        while current > 0 and self.heap[current][0] < self.heap[(current - 1) // 2][0]:
            self.heap[current], self.heap[(current - 1) // 2] = self.heap[(current - 1) // 2], self.heap[current]
            current = (current - 1) // 2
        self.heap[current] = element

    def remove(self):
        if self.size == 0:
            return (-1, "")
        popped = self.heap[0]
        if popped[0] is None:
            popped = (float('inf'), popped[1])
        else:
            popped = (popped[0], popped[1])
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return popped
    
    def min_heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.size and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def valrepr(self):
        if self.size == 0:
            return "No calls at the moment."
        else:
            heap_representation = ""
            for i in range(1, self.size+1):
                priority, recent_call = self.heap[i]
                heap_representation += f"{priority}:{recent_call}, "
            return f"MinHeap({heap_representation[:-2]})"

    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.size == 0: raise Exception("Heap is empty")
        return (self.heap[0][0], self.heap[0][1]) # return a tuple of (priority, dispatch_string)
    
    def dequeue(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return popped