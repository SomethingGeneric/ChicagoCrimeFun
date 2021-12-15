# Python3 implementation of Min heap

import sys, random

# sorted dispatch queue for the heap
class MinHeap:
    def __init__(self, maxsize=100000):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.FRONT = 1

        self.cheat = {}

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of the left child for the node currently at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    # Function to heapify the node at pos
    def minheapify(self, pos):

        # If the node is a non-leaf node and greater than any of its child
        if not self.isLeaf(pos):
            if (
                self.heap[pos] > self.heap[self.leftChild(pos)]
                or self.heap[pos] > self.heap[self.rightChild(pos)]
            ):

                # Swap with the left child and heapify the left child
                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minheapify(self.leftChild(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minheapify(self.rightChild(pos))

    # Function to build the min heap using the minheapify function
    def minheap(self):

        for pos in range(self.size // 2, 0, -1):
            self.minheapify(pos)

    # Function to insert a node into the heap
    def insert(self, element, rep):
        print("Inserting " + str(element) + " with " + str(rep))
        if self.size >= self.maxsize:
            return
        self.size += 1
        
        while self.has(element):
            element += 0.001
            print("Upping element value to " + str(element))
        print("-"*10)

        self.heap[self.size] = element

        self.cheat[element] = rep

        current = self.size

        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        self.minheap()

    # Function to remove and return the minimum element
    def remove(self):
        popped = self.heap[self.FRONT]
        rep = self.cheat[popped]
        self.cheat.pop(popped)

        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        if self.size != 0:
            self.minheapify(self.FRONT)
        # return popped
        return (popped, rep)

    # show next element, but don't remove it
    def peek(self):
        return (self.FRONT, self.cheat[self.heap[self.FRONT]])

    # nnhgnhngh
    def has(self, key):
        if key in self.cheat:
            return True
        else:
            return False


############################################################################

class MaxHeap:
    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):

        return 2 * pos

    def rightChild(self, pos):

        return (2 * pos) + 1

    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):

        self.heap[fpos], self.heap[spos] = (self.heap[spos], self.heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (
                self.heap[pos] < self.heap[self.leftChild(pos)]
                or self.heap[pos] < self.heap[self.rightChild(pos)]
            ):

                # Swap with the left child and heapify
                # the left child
                if self.heap[self.leftChild(pos)] > self.heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = element

        current = self.size

        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def pop(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        if self.size != 0:
            self.maxHeapify(self.FRONT)
        return popped

    def peek(self):
        return self.heap[self.FRONT]


class MaxHeapSort:
    def __init__(self):
        pass

    def sort(self, seq):
        heap = MaxHeap(len(seq))
        for i in seq:
            heap.insert(i)
        for i in range(len(seq)):
            seq[i] = heap.pop()
        return seq


if __name__ == "__main__":
    """minheap = MinHeap()
    minheap.insert(5, "five")
    minheap.insert(12, "twelve")
    minheap.insert(2, "two")
    minheap.insert(9, "nine")
    minheap.insert(11, "eleven")
    minheap.insert(13, "thirteen")
    minheap.insert(7, "seven")
    minheap.insert(6, "six")
    minheap.insert(8, "eight")
    print("The Min val is " + str(minheap.remove()))"""

    seq = []

    for i in range(20):
        n = random.randint(1, 100)
        if n not in seq:
            seq.append(n)

    print(seq)
    mxs = MaxHeapSort()
    copy_seq = seq[:]
    copy_seq.sort(reverse=True)
    seq = mxs.sort(seq)

    print("Python: " + str(copy_seq))

    print("Ours: " + str(seq))
