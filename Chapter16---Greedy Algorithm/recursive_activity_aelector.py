# 活动选择问题

# 使用递归的方法实现贪心算法
# 进行求解

def recursive_activity_selector(s, f, k, n):
    '''
    s: 活动的起始时间
    f: 活动的结束时间
    k: 当前已经存在于最优结构中的最晚活动
    n: 活动总数
    '''
    m = k + 1
    while m <= n and s[m] < f[k]:
        # 找到往后不冲突
        # 且结束时间最早的一场活动
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


# 迭代的贪心算法

def greedy_activity_selector(s, f):
    n = len(s) - 1
    A = [1]

    k = 1
    # 从第二个活动开始
    # 往后寻找当前活动相兼容的第一个活动
    # 直到所有活动搜索完毕
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A += [m]
            k = m
    return A


if __name__ == '__main__':
    s = [-1, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [-1, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    #A = recursive_activity_selector(s, f, 0, len(f) - 1)
    A = greedy_activity_selector(s, f)
    print(A)
