# 基本栈结构

class stack:
    def __init__(self):
        self.data = [0 for _ in range(16)]
        self.top = -1
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value


def stack_empty(S):
    if S.top == -1:
        return True
    else:
        return False


def push(S, x):
    S.top += 1
    S[S.top] = x


def pop(S):
    if stack_empty(S):
        raise OverflowError
    else:
        S.top -= 1
        return S[S.top + 1]


if __name__ == '__main__':
    S = stack()
    push(S, 2)
    push(S, 3)
    push(S, 1)
    print(pop(S))
    print(pop(S))
    print(pop(S))
