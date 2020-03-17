# 有向无环图的单源最短路径问题
from topological_sort import topological_sort
from relax_operation import \
    initialize_single_source, relax, GraphVertexEx, Graph, print_whole_path

def dag_shortest_paths(G, w, s):
    # 先对图G进行拓扑排序
    # 再按拓扑序进行一次松弛操作
    sorted_G = topological_sort(G)

    initialize_single_source(G, s)

    for u in sorted_G:
        for v in G.E[u]:
            relax(u, v, w)


def create_graph():
    G = Graph()
    w = {}

    r = GraphVertexEx('r')
    s = GraphVertexEx('s')
    t = GraphVertexEx('t')
    x = GraphVertexEx('x')
    y = GraphVertexEx('y')
    z = GraphVertexEx('z')

    G.V += [r, s, t, x, y, z]

    G.E[r] = [s, t]
    G.E[s] = [t, x]
    G.E[t] = [x, y, z]
    G.E[x] = [y, z]
    G.E[y] = [z]
    G.E[z] = []

    w[(r, s)] = 5
    w[(r, t)] = 3
    w[(s, t)] = 2
    w[(s, x)] = 6
    w[(t, x)] = 7
    w[(t, y)] = 4
    w[(t, z)] = 2
    w[(x, y)] = -1
    w[(x, z)] = 1
    w[(y, z)] = -2

    return G, w, s


if __name__ == '__main__':
    G, w, s = create_graph()
    dag_shortest_paths(G, w, s)
    print_whole_path(G, s)
