# 计数排序

def COUNTING_SORT(A, k):
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(len(A))]

    # 使得C包含A中每个元素的个数
    # 再计算C的累进个数
    # 这是得到的数值便是它的排名
    for j in range(len(A)):
        C[A[j]] += 1
    
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    
    return B

if __name__ == '__main__':
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    B = COUNTING_SORT(A, 5)
    print(B)
