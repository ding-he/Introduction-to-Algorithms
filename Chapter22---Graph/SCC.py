# 强连通分量
from graph import *
from DFS import GraphVertexEx, DFS, DFS_sorted


def SCC(G):
    DFS(G)
    GT = transpose_graph(G)
    print('----------')
    DFS_sorted(GT)


def transpose_graph(G):
    GT = Graph()

    vertex_map = {}

    for v in G.V:
        v_new = GraphVertexEx(v.value)
        # 记录时间戳
        v_new.d, v_new.f = v.d, v.f
        GT.V.append(v_new)
        GT.E[v_new] = []
        vertex_map[v] = v_new

    
    for u in G.V:
        for v in G.E[u]:
            GT.E[vertex_map[v]].append(vertex_map[u])
    
    return GT

def create_graph():
    G = Graph()

    a = GraphVertexEx('a')
    b = GraphVertexEx('b')
    c = GraphVertexEx('c')
    d = GraphVertexEx('d')
    e = GraphVertexEx('e')
    f = GraphVertexEx('f')
    g = GraphVertexEx('g')
    h = GraphVertexEx('h')

    G.V.append(a)
    G.E[a] = [b]

    G.V.append(b)
    G.E[b] = [c, e, f]

    G.V.append(c)
    G.E[c] = [d, g]

    G.V.append(d)
    G.E[d] = [c, h]

    G.V.append(e)
    G.E[e] = [a, f]

    G.V.append(f)
    G.E[f] = [g]

    G.V.append(g)
    G.E[g] = [f, h]

    G.V.append(h)
    G.E[h] = [h]

    return G


if __name__ == '__main__':
    G = create_graph()
    SCC(G)
