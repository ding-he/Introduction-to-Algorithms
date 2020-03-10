# 最长公共子序列问题

# 自底向上求解问题

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    # c代表当前前缀Xi与Yi最长公共子序列的个数
    # 首先c的第一行与第一列均为0
    # 因为当其中一个前缀长度为0是, 最长公共子序列也为0
    # b代表当前最长公共子序列是与哪个相关
    # '\':  表示与斜上方相关
    #       那么Xi与Yi的最长子序列
    #       为Xi-1与Yi-1的最长子序列+1
    # '-':  表示与左边元素相关
    #       那么Xi与Yi的最长子序列
    #       为Xi与Yi-1的最长子序列
    # '|':  表示与上边元素相关
    #       那么Xi与Yi的最长子序列
    #       为Xi-1与Yi的最长子序列
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    b = [['@' for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Xi == Yi
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\'
            # Xi != Yi
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '-'
    return c, b

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    
    if b[i][j] == '\\':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i - 1], end='')
    elif b[i][j] == '|':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

def print_matrix(matrix):
    for rows in matrix:
        for ele in rows:
            print(ele, end=' ')
        print()


if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'
    c, b = lcs_length(X, Y)
    print_lcs(b, X, len(X), len(Y))
    print()
    print_matrix(c)
    print_matrix(b)
