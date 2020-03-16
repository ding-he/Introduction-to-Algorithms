# 深度优先搜索
from graph import *

class GraphVertexEx(GraphVertex):
    def __init__(self, value=None):
        super(GraphVertexEx, self).__init__(value)
        self.color = None
        self.p = None
        self.d = None
        self.f = None

WHITE = 0
GRAY = 1
BLACK = 2

time = 0

def DFS(G):
    global time

    for u in G.V:
        u.color = WHITE
        u.p = None
    
    # 时间戳
    time = 0

    for u in G.V:
        if u.color == WHITE:
            DFS_VISIT(G, u)


def DFS_sorted(G):
    global time

    for u in G.V:
        u.color = WHITE
        u.p = None
    
    # 时间戳
    time = 0

    sorted_u = sorted(G.V, key=lambda u: u.f, reverse=True)

    for u in sorted_u:
        if u.color == WHITE:
            DFS_VISIT(G, u)

            # 一个强连通分量结束
            print('---------------')


def DFS_VISIT(G, u):
    global time

    time += 1
    u.d = time
    u.color = GRAY

    for v in G.E[u]:
        if v.color == WHITE:
            v.p = u
            DFS_VISIT(G, v)
    
    u.color = BLACK
    time += 1
    u.f = time
    print(u.value, '%d/%d' % (u.d, u.f))

def create_graph():
    G = Graph()

    u = GraphVertexEx('u')
    v = GraphVertexEx('v')
    w = GraphVertexEx('w')
    x = GraphVertexEx('x')
    y = GraphVertexEx('y')
    z = GraphVertexEx('z')

    G.V.append(u)
    G.E[u] = [v, x]

    G.V.append(v)
    G.E[v] = [y]

    G.V.append(w)
    G.E[w] = [y, z]

    G.V.append(x)
    G.E[x] = [v]

    G.V.append(y)
    G.E[y] = [x]

    G.V.append(z)
    G.E[z] = [z]

    return G


if __name__ == '__main__':
    G = create_graph()
    DFS(G)
