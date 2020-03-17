# 松弛操作

from graph import *
import sys

class GraphVertexEx(GraphVertex):
    def __init__(self, value=None):
        super(GraphVertexEx, self).__init__(value)
        self.d = None
        self.p = None
    
    def __lt__(self, other):
        return self.d < other.d

def initialize_single_source(G, s):
    for v in G.V:
        v.d = sys.maxsize
        v.p = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w[(u, v)]:
        v.d = u.d + w[(u, v)]
        v.p = u


def print_whole_path(G, s):
    for u in G.V:
        if u != s:
            print_path(G, s, u)
            print('(w = %d)' % u.d)



def print_path(G, s, v):
    if v == s:
        print(s.value, end=' ')
    elif v.p == None:
        print('no path')
    else:
        print_path(G, s, v.p)
        print(v.value, end=' ')
