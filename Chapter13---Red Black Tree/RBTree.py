from search_tree import tree_minimum

# 红黑树
class RBTree:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = None
        self.root = None
        self.nil = None


# 左旋 and 右旋
def left_rotate(T, x):
    y = x.right
    x.right = y.left

    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    
    y.left = x
    x.p = y


def right_rotate(T, x):
    y = x.left
    x.left = y.right

    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    
    y.right = x
    x.p = y


# 插入
def RB_insert(T, z):
    y = T.nil
    x = T.root

    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y

    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    
    z.left = T.nil
    z.right = T.nil
    z.color = 'R'
    RB_insert_fixup(T, z)

def RB_insert_fixup(T, z):
    while z.p.color == 'R':
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == 'R':
                z.p.color = 'B'
                y.color = 'B'
                z.p.p.color = 'R'
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                left_rotate(T, z)
            z.p.color = 'B'
            z.p.p.color = 'R'
            right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == 'R':
                z.p.color = 'B'
                y.color = 'B'
                z.p.p.color = 'R'
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                left_rotate(T, z)
            z.p.color = 'B'
            z.p.p.color = 'R'
            right_rotate(T, z.p.p)
    T.root.color = 'B'



# 删除节点
def RB_transplant(T, u, v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p

def RB_delete(T, z):
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        RB_transplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        RB_transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.p == z:
            x.p = y
        else:
            RB_transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        RB_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    
    if y_original_color == 'B':
        RB_delete_fixup(T, x)

def RB_delete_fixup(T, x):
    while x != T.root and x.color == 'B':
        if x == x.p.left:
            w = x.p.right
            if w.color == 'R':
                w.color = 'B'
                x.p.color = 'R'
                left_rotate(T, x.p)
                w = w.p.right
            
            if w.left.color == 'B' and w.right.color == 'B':
                w.color = 'R'
                x = x.p
            elif w.right.color == 'B':
                w.left.color = 'B'
                w.color = 'R'
                right_rotate(T, w)
                w = x.p.right
            w.color = x.p.color
            x.p.color = 'B'
            w.right.color = 'B'
            left_rotate(T, x.p)
            x = T.root
        else:
            w = x.p.left
            if w.color == 'R':
                w.color = 'B'
                x.p.color = 'R'
                right_rotate(T, x.p)
                w = w.p.left
            
            if w.right.color == 'B' and w.left.color == 'B':
                w.color = 'R'
                x = x.p
            elif w.left.color == 'B':
                w.right.color = 'B'
                w.color = 'R'
                left_rotate(T, w)
                w = x.p.left
            w.color = x.p.color
            x.p.color = 'B'
            w.left.color = 'B'
            right_rotate(T, x.p)
            x = T.root
    x.color = 'B'
