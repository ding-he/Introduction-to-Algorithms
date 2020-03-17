# Johnson算法
from bellman_ford import bellman_ford
from dijkstra import dijkstra
from relax_operation import Graph, GraphVertexEx

def johnson(G, w):
    # 计算G'
    # 对G加入一源节点s
    # 使得(s, v) = 0
    G1, s, w = compute_G(G, w)

    if False == bellman_ford(G1, w, s):
        raise "graph contain negative-weight cycle"
    else:
        # 计算h(v)
        h = {}
        for v in G1.V:
            h[v] = v.d
        
        # 更新w
        w1 = {}
        for u in G1.V:
            for v in G1.E[u]:
                w1[(u, v)] = w[u, v] + h[u] - h[v]
        
        n = len(G.V)
        D = [[0 for j in range(n)] for i in range(n)]
        # 使用Dijkstra算法
        for u in G.V:
            dijkstra(G, w1, u)

            for v in G.V:
                D[u.value - 1][v.value - 1] = v.d + h[v] - h[u]
        return D


def compute_G(G, w):
    G1 = Graph()
    G1.V = G.V.copy()
    G1.E = G.E.copy()

    s = GraphVertexEx(0)
    G1.V.append(s)
    G1.E[s] = [v for v in G.V]
    for v in G.V:
        w[(s, v)] = 0

    return G1, s, w

def create_graph():
    G = Graph()

    a = GraphVertexEx(1)
    b = GraphVertexEx(2)
    c = GraphVertexEx(3)
    d = GraphVertexEx(4)
    e = GraphVertexEx(5)

    G.V += [a, b, c, d, e]
    w = {}

    def AddVertex(u, v, weight):
        if u not in G.E:
            G.E[u] = []
        G.E[u].append(v)
        w[(u, v)] = weight
    
    AddVertex(a, b, 3)
    AddVertex(a, c, 8)
    AddVertex(a, e, -4)
    AddVertex(b, d, 1)
    AddVertex(b, e, 7)
    AddVertex(c, b, 4)
    AddVertex(d, a, 2)
    AddVertex(d, c, -5)
    AddVertex(e, d, 6)

    return G, w

if __name__ == '__main__':
    G, w = create_graph()
    D = johnson(G, w)

    for d in D:
        print(d)
