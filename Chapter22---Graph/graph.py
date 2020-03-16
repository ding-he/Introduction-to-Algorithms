# 图数据结构定义

class Graph:
    def __init__(self):
        self.V = []
        self.E = {}


class GraphVertex:
    def __init__(self, value=None):
        self.value = value
