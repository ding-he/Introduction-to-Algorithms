# 桶排序

def BUCKET_SORT(A):
    # 桶排序是把所有的数分成n等分
    # 这n等分是按照数据分布情况来的
    # 并且n等分的数据已经存在大小顺序
    # 这里假定数据是均匀分布在[0, 1)之间

    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        ind = int(n*A[i])
        B[ind].append(A[i])
    
    for i in range(n):
        B[i] = sorted(B[i])
    
    for i in range(1, n):
        B[0] += B[i]
    
    return B[0]


if __name__ == '__main__':
    A = [.78, .17, .39, .26, .72, .94, .21, .12, .23, .68]
    B = BUCKET_SORT(A)
    print(B)
