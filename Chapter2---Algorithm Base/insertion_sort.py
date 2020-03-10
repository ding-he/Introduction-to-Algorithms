# insertion sort

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]

        # 将A[j]插入到A[0:j]已排序的数组中
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

A = insertion_sort([5, 2, 4, 6, 1])
print(A)
