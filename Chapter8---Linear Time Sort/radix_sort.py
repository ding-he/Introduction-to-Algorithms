# 基数排序

def RADIX_SORT(A, d):
    # 对数字从低位到高位进行单位排序
    # 并且需要使用稳定的稳定的排序方法
    for i in range(d):
        A = COUNTING_SORT_EX(A, i, 9)
        
    return A

def COUNTING_SORT_EX(A, d, k):
    C = [0 for _ in range(k + 1)]
    B = [0 for _ in range(len(A))]

    # 与普通的计数排序不同的是
    # 这里比较的是数的第d位

    for j in range(len(A)):
        t = A[j] // 10**d % 10
        C[t] += 1
    
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A) - 1, -1, -1):
        t = A[j] // 10**d % 10
        B[C[t] - 1] = A[j]
        C[t] -= 1
    
    return B


if __name__ == '__main__':
    A = [329, 457, 657, 839, 436, 720, 355]
    B = RADIX_SORT(A, 3)
    print(B)