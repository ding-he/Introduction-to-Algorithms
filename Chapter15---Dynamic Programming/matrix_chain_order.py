# 矩阵链乘法问题
import sys

# 递归方法求解
def recursive_matrix_chain(p, i, j):
    if i == j:
        return 0

    m[i][j] = sys.maxsize
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k) + \
            recursive_matrix_chain(p, k + 1, j) + \
            p[i - 1]*p[k]*p[j]
        
        if q < m[i][j]:
            m[i][j] = q
    return m[i][j]


# 带备忘的自顶向下
def memoized_matrix_chain(p):
    n = len(p) - 1
    m = [[sys.maxsize for j in range(n + 1)] for i in range(n + 1)]

    return lookup_chain(m, p, 1, n)

def lookup_chain(m, p, i, j):
    if m[i][j] < sys.maxsize:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookup_chain(m, p, i, k) + \
                lookup_chain(m, p, k + 1, j) + \
                p[i - 1]*p[k]*p[j]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


# 自底向上求解

def matrix_chain_order(p):
    # p是一个线性表
    # 表示了矩阵链每个矩阵的行列数
    # 它的长度是矩阵个数n + 1
    n = len(p) - 1
    
    # m是矩阵链[i, j]乘法所付出的代价
    # s是矩阵链[i, j]中最佳分界点k
    # 使得[i, k], [k + 1, j]的代价最小
    # m[i, i]这个代价的是自身和自身, 代价则为0
    # 这是初始条件
    m = [[0 for j in range(n + 1)] for i in range(n + 1)]
    s = [[0 for j in range(n + 1)] for i in range(n + 1)]

    # 矩阵链长度l从2计算到n
    for l in range(2, n + 1):
        # i代表[i, j]这个矩阵链的起始位置
        # 它是从1到i - l + 1
        # j便是末尾位置
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize

            # k的范围是分界点, 是从i到j - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print('A', i, sep='', end='')
    else:
        print('(',  end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')',  end='')


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    n = len(p) - 1
    #m, s = matrix_chain_order(p)
    #print(m[1][n])
    #print_optimal_parens(s, 1, n)
    m = memoized_matrix_chain(p)
    print(m)
