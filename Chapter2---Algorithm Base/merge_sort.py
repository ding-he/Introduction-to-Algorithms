# 归并排序

import sys

def merge(A, p, q, r):
    # 分别取出两个数组的左右
    L = A[p: q + 1]
    R = A[q + 1: r + 1]

    # 添加哨兵
    L.append(sys.maxsize)
    R.append(sys.maxsize)

    i = j = 0
    # 将两个数组进行归并
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A[p: r + 1]

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        A = merge_sort(A, p, q)
        A = merge_sort(A, q + 1, r)
        A[p: r + 1] = merge(A, p, q, r)
    return A

A = [5, 2, 4, 6, 1]
A = merge_sort(A, 0, len(A) - 1)
print(A)
