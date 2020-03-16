# Kruskal算法
# 最小生成树问题
from graph import *

class GraphVertexEx(GraphVertex):

    def __init__(self, value=None):
        super(GraphVertexEx, self).__init__(value)
        self.key = None
        self.p = None

    def __lt__(self, other):
        return self.key < other.key

def MST_Kruskal(G, w):
    A = []
    S = []
    total_w = 0

    # 对图中每个节点创建一个集合
    for v in G.V:
        s = [v]
        S.append(s)
    
    # 对所有边按权重降序排序
    w_sorted = sorted(w.items(), key=lambda e: e[1])

    # 每次都将与A的轻量边加入
    for (u, v), weight in w_sorted:
        s_u = FIND_SET(S, u)
        s_v = FIND_SET(S, v)
        if s_u != s_v:
            A += [(u, v)]
            total_w += weight
            s_u += s_v
            S.remove(s_v)
    
    return A, total_w

def FIND_SET(S, u):
    for s in S:
        if u in s:
            return s
    return None


def create_graph():
    G = Graph()
    w = {}
    
    a = GraphVertexEx('a')
    b = GraphVertexEx('b')
    c = GraphVertexEx('c')
    d = GraphVertexEx('d')
    e = GraphVertexEx('e')
    f = GraphVertexEx('f')
    g = GraphVertexEx('g')
    h = GraphVertexEx('h')
    i = GraphVertexEx('i')

    G.V.append(a)
    G.E[a] = [b, h]

    G.V.append(b)
    G.E[b] = [a, c, h]
    
    G.V.append(c)
    G.E[c] = [b, d, f, i]

    G.V.append(d)
    G.E[d] = [c, e, f]

    G.V.append(e)
    G.E[e] = [d, f]

    G.V.append(f)
    G.E[f] = [c, d, e, g]

    G.V.append(g)
    G.E[g] = [f, h, i]

    G.V.append(h)
    G.E[h] = [a, b, g, i]

    G.V.append(i)
    G.E[i] = [c, g, h]
    
    w[(a, b)] = 4
    w[(a, h)] = 8
    w[(b, h)] = 11
    w[(b, c)] = 8
    w[(h, i)] = 7
    w[(h, g)] = 1
    w[(i, g)] = 6
    w[(c, i)] = 2
    w[(c, f)] = 4
    w[(g, f)] = 2
    w[(c, d)] = 7
    w[(d, f)] = 14
    w[(d, e)] = 9
    w[(e, f)] = 10

    return G, w

if __name__ == '__main__':
    G, w = create_graph()
    A, total_w = MST_Kruskal(G, w)
    
    print('total weight =', total_w)

    for u, v in A:
        print('(' + u.value, v.value + ')')
