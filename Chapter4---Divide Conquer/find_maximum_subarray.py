# 最大子数组
import sys

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -sys.maxsize
    s = 0

    # 向左寻找最大的子数组
    for i in range(mid, low - 1, -1):
        s += A[i]
        if s > left_sum:
            left_sum = s
            max_left = i

    right_sum = -sys.maxsize
    s = 0

    # 向右寻找最大的子数组
    for j in range(mid + 1, high + 1):
        s += A[j]
        if s > right_sum:
            right_sum = s
            max_right = j
    
    # 返回跨越中间点的最大子数组
    return max_left, max_right, left_sum + right_sum

def find_maximum_subarray(A, low, high):
    if high == low:
        # 递归结束条件, 单个元素本身便是最大子数组
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        # 递归过程
        # 分别问题看作三个子问题
        # 最大子数组一定存在于
        # 左子数组, 右子数组, 跨越中间点的子数组之中的一个
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        # 合并过程
        # 分别比较三种情况下的三个子问题, 可以得到数组中的最大子数组
        sub_sum = max(left_sum, right_sum, cross_sum)
        if sub_sum == left_sum:
            return left_low, left_high, left_sum
        elif sub_sum == right_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -2, 12, -5, -22, 15, -4, 7][0:10]
low, high, sub_sum = find_maximum_subarray(A, 0, len(A) - 1)
print('(%d, %d) = %d' % (low, high, sub_sum))
print(A[low: high + 1])

