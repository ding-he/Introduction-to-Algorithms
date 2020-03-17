# Bellman-Ford算法
# 单源最短路径问题
from relax_operation import \
    initialize_single_source, relax, GraphVertexEx, Graph, print_whole_path

def bellman_ford(G, w, s):
    initialize_single_source(G, s)

    # 对所有边进行松弛操作
    # 执行|V| - 1遍
    # 可以使得路径的v.d达到最短路径

    for _ in range(len(G.V) - 1):
        for u in G.V:
            for v in G.E[u]:
                relax(u, v, w)
    
    # 最后检查是否存在负数环
    # 如果不存在, 则必定返回True
    for u in G.V:
        for v in G.E[u]:
            if v.d > u.d + w[(u, v)]:
                return False
    return True


def create_graph():
    G = Graph()
    w = {}

    s = GraphVertexEx('s')
    t = GraphVertexEx('t')
    x = GraphVertexEx('x')
    y = GraphVertexEx('y')
    z = GraphVertexEx('z')

    G.V += [s, t, x, y, z]

    G.E[s] = [t, y]
    G.E[t] = [x, y, z]
    G.E[x] = [t]
    G.E[y] = [x, z]
    G.E[z] = [s, x]

    w[(s, t)] = 6
    w[(s, y)] = 7
    w[(t, x)] = 5
    w[(t, y)] = 8
    w[(t, z)] = -4
    w[(x, t)] = -2
    w[(y, x)] = -3
    w[(y, z)] = 9
    w[(z, s)] = 2
    w[(z, x)] = 7

    return G, w, s


if __name__ == '__main__':
    G, w, s = create_graph()
    if bellman_ford(G, w, s):
        print_whole_path(G, s)
    else:
        print('图中存在环')
