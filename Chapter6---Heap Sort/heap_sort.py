# 堆排序算法
from build_heap import Heap, BUILD_MAX_HEAP, MAX_HEAPIFY

def HEAPSORT(A):
    # 对数组直接建立堆结构
    # 再将每次的最大值放入数组的最末尾处
    # 最后将数组首处重新建立堆结构
    # 如此往复
    A = BUILD_MAX_HEAP(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heapsize -= 1
        A = MAX_HEAPIFY(A, 0)
    
    return A

if __name__ == '__main__':
    A = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    A = HEAPSORT(A)
    print(A)
