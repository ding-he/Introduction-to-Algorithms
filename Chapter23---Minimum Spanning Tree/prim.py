# Prim算法
# 最小生成树
from graph import Graph
from kruskal import create_graph, GraphVertexEx
import sys
import heapq

def MST_Prim(G, w, r):
    for u in G.V:
        u.key = sys.maxsize
        u.p = None
    
    r.key = 0

    # 最小优先队列
    Q = G.V.copy()
    heapq.heapify(Q)

    while Q:
        u = heapq.heappop(Q)
        for v in G.E[u]:
            if v in Q:
                weight = w[(u, v)] if (u, v) in w else w[(v, u)]
                if weight < v.key:
                    v.p = u
                    v.key = weight

                    # 隐性的改变优先队列
                    Q.remove(v)
                    heapq.heappush(Q, v)

def print_mst(G, r):
    for u in G.V:
        if u != r:
            print('(%s, %s)' % (u.value, u.p.value))


if __name__ == '__main__':
    G, w = create_graph()
    r = G.V[0]

    MST_Prim(G, w, r)
    print_mst(G, r)
