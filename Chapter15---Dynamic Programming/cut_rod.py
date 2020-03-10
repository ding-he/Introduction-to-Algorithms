'''
钢条切割问题
'''

# 使用自顶向下递归方式实现
# 时间复杂度为O(2^n)

def cut_rod(p, n):
    '''
    p: 钢条价格表
    n: 所要切割钢条的总长度
    '''
    if n == 0:
        return 0
    q = -1
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    
    return q


# 使用带备忘的自顶向下方法
# 可以得到复杂度为O(n2)

def memoized_cut_rod(p, n):
    # 利用r记录已经计算过的子问题的解
    r = [-1 for _ in range(n + 1)]

    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    # 每次遇到算过的子问题直接返回
    # 而不必计算
    if r[n] >= 0:
        return r[n]
    
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    
    r[n] = q
    return q


# 自底向上方法
# 从子问题开始求解
# 再重构出问题的解
def bottom_up_cut_rpd(p, n):
    r = [0 for _ in range(n + 1)]
    
    for j in range(1, n + 1):
        q = -1
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    
    return r[n]


# 带重构解的自底向上方案
def extended_bottom_up_cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    s = r.copy()
    
    for j in range(1, n + 1):
        q = -1
        for i in range(j):
            if q < p[i] + r[j - i - 1]:
                q = p[i] + r[j - i - 1]
                s[j] = i + 1
        r[j] = q
    
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    q = r[n]
    while n > 0:
        print(s[n])
        n -= s[n]
    
    return q



if __name__ == '__main__':
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    #q = cut_rod(p, 7)
    #q = memoized_cut_rod(p, 7)
    #q = bottom_up_cut_rpd(p, 7)
    q = print_cut_rod_solution(p, 7)
    print(q)
