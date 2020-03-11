# 使用贪心算法分析霍夫曼编码问题
# 构造最优编码树
import heapq

class TreeNode:
    def __init__(self, freq=0, data=None):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman(C):
    n = len(C)
    Q = C
    heapq.heapify(Q)

    # 每次都从堆中取出最小的两个码
    # 把它们作为一个叶子节点
    # 再将它们的合并内容放入堆中
    for _ in range(n - 1):
        z = TreeNode()
        z.left = x = heapq.heappop(Q)
        z.right = y = heapq.heappop(Q)
        z.freq = x.freq + y.freq
        heapq.heappush(Q, z)
    return Q[0]


def create_data(character, frequent):
    C = []
    for c, f in zip(character, frequent):
        node = TreeNode(f, c)
        C.append(node)
    return C


def print_code(node, code):
    if node:
        code.append(0)
        print_code(node.left, code)
        code.pop()
        if node.data:
            _print_code(node.data, code)
        code.append(1)
        print_code(node.right, code)
        code.pop()

def _print_code(char, code):
    s_code = ''
    for c in code:
        s_code += str(c)
    print(char, '->', s_code)


if __name__ == '__main__':
    character = ['a', 'b', 'c', 'd', 'e', 'f']
    frequent = [45, 13, 12, 16, 9, 5]
    C = create_data(character, frequent)
    treeNode = huffman(C)
    print_code(treeNode, [])
