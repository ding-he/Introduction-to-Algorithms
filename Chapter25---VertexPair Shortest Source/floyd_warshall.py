# Floyd-Warshall算法
# D(k)[i][j] =  |   W[i][j]     k == 0
#               |   min(D(k - 1)[i][j], D(k - 1)[i][k] + D(k - 1)[k][j])    k != 0


def floyd_warshall(W):
    n = len(W)
    D = W

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


# 前驱迭代
# T(0)[i][j] = |  0   i != j and (i, j) not in E
#              |  1   i == j or  (i, j) in E
# T(k)[i][j] = T(k - 1)[i][j] | (T(k - 1)[i][k] & T(k - 1)[k][j])
def transitive_closure(G):
    n = len(G.V)
    T = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j or (i, j) in G.E:
                T[i][j] = 1
            else:
                T[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] | (T[i][k] & T[k][j])
    return T


if __name__ == '__main__':
    inf = float('inf')
    W = [
        [0, 3, 8, inf, -4],
        [inf, 0, inf, 1, 7],
        [inf, 4, 0, inf, inf],
        [2, inf, -5, 0, inf],
        [inf, inf, inf, 6, 0]
    ]
    D = floyd_warshall(W)
    for d in D:
        print(d)
