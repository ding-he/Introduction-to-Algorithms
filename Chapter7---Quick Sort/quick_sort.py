# 快速排序
# 把数组分成两部分, 一部分都大于另一部分
# 并有一个元素介于两者之间
# 最后使用递归的方法分别堆这两部分进行排序
import random

def QUICKSORT(A, p, r):
    if p < r:
        A, q = PARTITION(A, p, r)
        A = QUICKSORT(A, p, q - 1)
        A = QUICKSORT(A, q + 1, r)
    return A

def PARTITION(A, p, r):
    # 将这部分数组分成[p, i]小的一部分
    # [i + 1, j]作为大的一部分
    # [r]作为哨兵
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return A, i + 1

def RANDOMIZED_PARTITION(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return PARTITION(A, p, r)

def RANDOMIZED_QUICKSORT(A, p, r):
    if p < r:
        A, q = RANDOMIZED_PARTITION(A, p, r)
        A = RANDOMIZED_QUICKSORT(A, p, q - 1)
        A = RANDOMIZED_QUICKSORT(A, q + 1, r)
    return A



if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    RA = RANDOMIZED_QUICKSORT(A, 0, len(A) - 1)
    A = QUICKSORT(A, 0, len(A) - 1)
    print(A)
    print(RA)
