# 优先级队列(最大)
import sys
from build_heap import *

class PriorityQueue:
    def __init__(self):
        self.heap = Heap([])
        self.heap.heapsize = 0
    
    def __str__(self):
        return str(self.heap)
    
    def HeapMaximum(self):
        # 最大值元素便是堆结构中的首元素
        return self.heap[0]
    
    def HeapExtractMax(self):
        # 将首元素取出后, 将原来的末尾元素放在首部
        # 并重新建立堆结构即可
        if self.heap.heapsize <= 0:
            raise OverflowError
        m, self.heap[0] = self.heap[0], self.heap[self.heap.heapsize - 1]
        self.heap.heapsize -= 1
        MAX_HEAPIFY(self.heap, 0)
        return m
    
    def HeapIncreaseKey(self, i, key):
        # 往上不断地修正堆结构
        if key < self.heap[i]:
            raise Exception
        self.heap[i] = key
        
        while i >= 0 and PARENT(i) >= 0 and self.heap[PARENT(i)] < self.heap[i]:
            self.heap[i], self.heap[PARENT(i)] = self.heap[PARENT(i)], self.heap[i]
            i = PARENT(i)

    def MaxHeapInsert(self, key):
        # 在末尾插入一个很小的
        # 再把它提升到key
        self.heap.heapsize += 1
        self.heap.append(-sys.maxsize)
        self.HeapIncreaseKey(self.heap.heapsize - 1, key)

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.MaxHeapInsert(1)
    pq.MaxHeapInsert(2)
    pq.MaxHeapInsert(5)
    pq.MaxHeapInsert(4)
    print(pq)
    print(pq.HeapExtractMax())
    print(pq.HeapExtractMax())
    print(pq.HeapExtractMax())
    print(pq.HeapExtractMax())  
