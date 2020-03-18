# LUP分解计算矩阵乘法
# P转置矩阵
# L下三角矩阵
# U上三角矩阵
# Ax = b <=> PAx = LUx = Ly = Pb = b[p]

def lup_solve(L, U, p, b):
    n = len(L)
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    for i in range(n):
        s = 0
        for j in range(i - 1):
            s += L[i][j] * y[j]
        y[i] = b[p[i]] - s
    
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i, n - 1):
            s += U[i][j] * x[j]
        x[i] = (y[i] - s) / U[i][j]
    return x
