# 拓扑排序
from graph import *
from DFS import GraphVertexEx, DFS


# 有向拓扑排序一定是无环图
def topological_sort(G):
    DFS(G)

    out = sorted(G.V, key=lambda v: v.f, reverse=True)

    return out


def create_graph():
    G = Graph()

    nk = GraphVertexEx('内裤')
    kz = GraphVertexEx('裤子')
    yd = GraphVertexEx('腰带')
    cy = GraphVertexEx('衬衣')
    ld = GraphVertexEx('领带')
    jk = GraphVertexEx('夹克')
    wz = GraphVertexEx('袜子')
    x = GraphVertexEx('鞋')
    sb = GraphVertexEx('手表')

    G.V.append(nk)
    G.E[nk] = [kz, x]

    G.V.append(kz)
    G.E[kz] = [yd, x]

    G.V.append(yd)
    G.E[yd] = [jk]

    G.V.append(cy)
    G.E[cy] = [yd, ld]

    G.V.append(ld)
    G.E[ld] = [jk]

    G.V.append(jk)
    G.E[jk] = []

    G.V.append(wz)
    G.E[wz] = [x]

    G.V.append(x)
    G.E[x] = []

    G.V.append(sb)
    G.E[sb] = []

    return G


if __name__ == '__main__':
    G = create_graph()
    sort_graph = topological_sort(G)

    print_list = ['%s %d/%d' % (u.value, u.d, u.f) for u in sort_graph]
    print(print_list)
