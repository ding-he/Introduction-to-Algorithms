# 广度优先搜索
from graph import *
import queue
import sys

class GraphVertexEx(GraphVertex):
    def __init__(self, value=None):
        super(GraphVertexEx, self).__init__(value)
        self.color = None
        self.d = None
        self.p = None


WHITE = 0
GRAY = 1
BLACK = 2


def BFS(G, s):
    # 对每个节点进行初始化
    for u in G.V:
        if u == s:
            continue
        u.color = WHITE
        u.d = sys.maxsize
        u.p = None
    
    # 当前节点正在被访问
    # 染成灰色
    s.color = GRAY
    s.d = 0
    s.p = None

    Q = queue.Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in G.E[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.p = u
                Q.put(v)
        u.color = BLACK
        print(u.value)

def print_path(G, s, v):
    if v == s:
        print(s.value)
    elif v.p == None:
        print('no path')
    else:
        print_path(G, s, v.p)
        print(v.value)

def create_graph():
    G = Graph()

    r = GraphVertexEx('r')
    s = GraphVertexEx('s')
    t = GraphVertexEx('t')
    u = GraphVertexEx('u')
    v = GraphVertexEx('v')
    w = GraphVertexEx('w')
    x = GraphVertexEx('x')
    y = GraphVertexEx('y')

    G.V.append(r)
    G.E[r] = [s, v]

    G.V.append(s)
    G.E[s] = [r, w]

    G.V.append(t)
    G.E[t] = [u, w, x]

    G.V.append(u)
    G.E[u] = [t, x, y]

    G.V.append(v)
    G.E[v] = [r]

    G.V.append(w)
    G.E[w] = [s, t, x]

    G.V.append(x)
    G.E[x] = [t, u, w, y]

    G.V.append(y)
    G.E[y] = [u, x]

    return G, s, y


if __name__ == '__main__':
    G, s, y = create_graph()
    BFS(G, s)
    print('--------')
    print_path(G, s, y)
