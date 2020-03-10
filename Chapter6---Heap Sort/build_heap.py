# 构建堆数据结构

class Heap:
    def __init__(self, A):
        self.A = A
        self.heapsize = 0
    
    def __getitem__(self, key):
        return self.A[key]
    
    def __setitem__(self, key, value):
        self.A[key] = value
    
    def __len__(self):
        return len(self.A)
    
    def __str__(self):
        return str(self.A)
    
    def append(self, key):
        self.A.append(key)

def PARENT(i):
    return (i - 1) // 2

def LEFT(i):
    return (i + 1) * 2 - 1

def RIGHT(i):
    return (i + 1) * 2

def MAX_HEAPIFY(A, i):
    l = LEFT(i)
    r = RIGHT(i)

    # 通过比较当前节点与左右子节点的大小
    # 来判断要与谁交换
    # 最后再递归调用大的那一方
    # 如果当前节点最大, 则可以立即返回
    if l < A.heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < A.heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        A = MAX_HEAPIFY(A, largest)
    return A

def BUILD_MAX_HEAP(A):
    A.heapsize = len(A)

    # 从末尾开始不断地向前构建堆
    # 最后所有元素都具有堆的结构
    for i in range(len(A)//2 - 1, -1, -1):
        A = MAX_HEAPIFY(A, i)
    
    return A

if __name__ == '__main__':
    A = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    A = BUILD_MAX_HEAP(A)
    print(A)
