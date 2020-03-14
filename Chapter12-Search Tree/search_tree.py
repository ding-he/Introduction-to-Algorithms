# 二叉搜索树
class Tree:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.root = None


# 查找
def tree_search(x, k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


# 迭代方法查找
def iterative_tree_search(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


# 最大关键字 and 最小关键字
def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x


# 后继 and 前驱
def tree_successor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y


# 插入 and 删除
def tree_insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.key = z
    else:
        y.right = z

def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p

def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y

