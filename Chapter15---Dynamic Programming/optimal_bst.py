# 做优二叉搜索树问题
import sys

def optimal_bst(p, q, n):
    # p: 搜索得到的元素概率1~n
    # q: 搜索不到的元素概率0~n

    # e表示[i, j]子树的搜索代价
    # w表示[i, j]子树所有元素出现的概率和
    # root表示[i, j]子树所具有的最优搜索根节点k
    e = [[0.0 for j in range(n + 1)] for i in range(n + 2)]
    w = [[0.0 for j in range(n + 1)] for i in range(n + 2)]
    root= [[0 for j in range(n + 1)] for i in range(n + 1)]

    # 当子树只剩空子树时
    # 包含唯一搜索不到的元素di-1
    # 它的概率便是qi-1
    # 代价为1*qi-1
    for i in range(n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    
    # 计算长度从1到n
    for l in range(1, n + 1):
        # 那么[i, j]它的起始范围是从1到n-l+1
        # 末尾范围为j
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = sys.maxsize
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            # r从[i, j]进行搜索, 找出最优代价
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root


def print_matrix(matrix):
    for rows in matrix:
        for ele in rows:
            if isinstance(ele, float):
                print('%.2f' % ele, end=' ')
            else:
                print(ele, end=' ')
        print()


if __name__ == '__main__':
    p = [-1.0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    e, root = optimal_bst(p, q, len(p) - 1)
    print_matrix(e)
    print_matrix(root)
