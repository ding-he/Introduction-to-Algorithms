# 矩阵乘法
# 解决节点对最短路径问题

# 迭代问题
# L(m)[i][j] = min(L(m - 1)[i][k] + W[k][j])  1 <= k <= n

def extend_shortest_paths(L, W):
    n = len(L)
    L1 = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            L1[i][j] = float('inf')

            for k in range(n):
                L1[i][j] = min(L1[i][j], L[i][k] + W[k][j])
    return L1


def square_matrix_multiple(A, B):
    pass


def slow_all_pairs_shortest_paths(W):
    n = len(W)

    # 初始状态
    L = W

    # compute L(1) ~ L(m) = L(n - 1)
    for _ in range(n-2):
        L = extend_shortest_paths(L, W)

    return L


def faster_all_pairs_shortest_paths(W):
    n = len(W)
    L = W
    m = 1

    while m < n - 1:
        L = extend_shortest_paths(L, L)
        m *= 2
    return L


if __name__ == '__main__':
    inf = float('inf')
    W = [
        [0, 3, 8, inf, -4],
        [inf, 0, inf, 1, 7],
        [inf, 4, 0, inf, inf],
        [2, inf, -5, 0, inf],
        [inf, inf, inf, 6, 0]
    ]
    #L = slow_all_pairs_shortest_paths(W)
    L = faster_all_pairs_shortest_paths(W)
    for l in L:
        print(l)
