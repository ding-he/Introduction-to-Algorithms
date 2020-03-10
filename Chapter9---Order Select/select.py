# 期望为线性时间的选择算法

import random

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

def RANDOMIZED_SELECT(A, p, r, i):
    # 与快速排序一样
    # 将数组分为小半部分和大半部分
    # 若这个数是中间哨兵位则直接返回
    # 否则递归的找其中一部分即可
    if p == r:
        return A[p]
    A, q = RANDOMIZED_PARTITION(A, p, r)
    k = q - p + 1
    if i == k:
        # 中间哨兵
        return A[q]
    elif i < k:
        # 落在小半部分
        return RANDOMIZED_SELECT(A, p, q - 1, i)
    else:
        # 落在大半部分
        return RANDOMIZED_SELECT(A, q + 1, r, i - k)


if __name__ == '__main__':
    A = [2, 8, 7, 1, 3, 5, 6, 4]
    value = RANDOMIZED_SELECT(A, 0, len(A) - 1, 3)
    print(value)
