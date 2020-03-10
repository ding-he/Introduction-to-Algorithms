# Straseen矩阵相乘
import numpy as np
import time


def straseen_matrix_multiple(A, B):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=int)

    if n == 1:
        # 1x1矩阵相乘则直接相乘
        C[0, 0] = A[0, 0] * B[0, 0]
    else:
        # 将A, B, C三个矩阵分别分为4个n/2*n/2的子矩阵
        # 那么以中间点mid来分的话, 可以分成
        # (1, 1): [0: mid][0: mid]
        # (1, 2): [0: mid][mid: n]
        # (2, 1): [mid: n][0: mid]
        # (2, 2): [mid: n][mid: n]
        mid = n // 2

        # 计算子矩阵之间的和或差, 共10个
        S1 = B[0: mid, mid: n] - B[mid: n, mid: n]
        S2 = A[0: mid, 0: mid] + A[0: mid, mid: n]
        S3 = A[mid: n, 0: mid] + A[mid: n, mid: n]
        S4 = B[mid: n, 0: mid] - B[0: mid, 0: mid]
        S5 = A[0: mid, 0: mid] + A[mid: n, mid: n]
        S6 = B[0: mid, 0: mid] + B[mid: n, mid: n]
        S7 = A[0: mid, mid: n] - A[mid: n, mid: n]
        S8 = B[mid: n, 0: mid] + B[mid: n, mid: n]
        S9 = A[0: mid, 0: mid] - A[mid: n, 0: mid]
        S10 = B[0: mid, 0: mid] + B[0: mid, mid: n]

        # 递归计算7个子矩阵P的值
        P1 = straseen_matrix_multiple(A[0: mid, 0: mid], S1)
        P2 = straseen_matrix_multiple(S2, B[mid: n, mid: n])
        P3 = straseen_matrix_multiple(S3, B[0: mid, 0: mid])
        P4 = straseen_matrix_multiple(A[mid: n, mid: n], S4)
        P5 = straseen_matrix_multiple(S5, S6)
        P6 = straseen_matrix_multiple(S7, S8)
        P7 = straseen_matrix_multiple(S9, S10)

        # 通过P计算C的四个子矩阵的值
        C[0: mid, 0: mid] = P5 + P4 - P2 + P6
        C[0: mid, mid: n] = P1 + P2
        C[mid: n, 0: mid] = P3 + P4
        C[mid: n, mid: n] = P5 + P1 - P3 - P7
    
    return C

A = np.array([
    [2, 1, 3, 2],
    [5, 2, 1, 1],
    [0, 1, 2, 1],
    [5, 6, 2, 1]
])
B = np.array([
    [4, 2, 1, 2],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [6, 4, 3, 2]
])

# n = 128
# A = np.random.randn(n, n)
# B = np.random.randn(n, n)

start = time.time()
C = straseen_matrix_multiple(A, B)
print(C)
end = time.time()
print(end - start)

start = time.time()
C = np.matmul(A, B)
print(C)
end = time.time()
print(end - start)
        