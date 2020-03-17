# Dijkstra算法
# 非负权重单源最短路径
import heapq
from relax_operation import \
    initialize_single_source, relax, GraphVertexEx, Graph, print_whole_path


def dijkstra(G, w, s):
    initialize_single_source(G, s)

    # 维持一个集合S
    # 每次从V - S中取出u.d最小的节点
    # 对u的每条边进行松弛操作
    # 并把u加入到集合S中
    # 当S = V时, 保证所有u.d为最短路径

    S = []
    Q = G.V.copy()
    heapq.heapify(Q)

    while Q:
        u = heapq.heappop(Q)
        S.append(u)

        for v in G.E[u]:
            relax(u, v, w)

            # 隐含的decrease_key
            if v in Q:
                Q.remove(v)
                heapq.heappush(Q, v)


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
    G.E[t] = [x, y]
    G.E[x] = [z]
    G.E[y] = [t, x, z]
    G.E[z] = [s, x]

    w[(s, t)] = 10
    w[(s, y)] = 5
    w[(t, x)] = 1
    w[(t, y)] = 2
    w[(x, z)] = 4
    w[(y, t)] = 3
    w[(y, x)] = 9
    w[(y, z)] = 2
    w[(z, s)] = 7
    w[(z, x)] = 6

    return G, w, s


if __name__ == '__main__':
    G, w, s = create_graph()
    dijkstra(G, w, s)
    print_whole_path(G, s)
