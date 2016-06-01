from math import floor

class MaxHeap(object):
    
    a = []
    size = 0
    
    def __init__(self, a, size):
        self.size = size
        self.a = a
        self.build()

    def parent(self, i):
        return floor(i/2)

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def max(self):
        return self.a[0]

    def swap(self, i, j):
        tmp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = tmp

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.size and self.a[l] >= self.a[i]:
            largest = l
        else:
            largest = i

        if r < self.size and self.a[r] >= self.a[largest]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)

    def build(self):
        for i in range(floor(self.size / 2), -1, -1):
            self.heapify(i)

    def sort(self):
        l = self.size
        for i in range(l):
            self.swap(0, self.size-1)
            self.size -= 1
            self.heapify(0)

        self.size = l

        return self.a

    def swim(self, i):
        if i > 0 and self.a[i] > self.a[self.parent(i)]:
            self.swap(i, self.parent(i))
            self.swim(self.parent(i))

    def insert(self, x):
        self.a.append(x)
        self.size += 1
        self.swim(self.size - 1)

if __name__ == "__main__":

    a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    
    heap = MaxHeap(a, len(a))
    print([i for i in heap.a])
    print(heap.max())
    heap.insert(18)
    print(heap.a)
    print(heap.sort())
