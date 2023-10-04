import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

def _union(x,y):
    px = find(x)
    py = find(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def solution():
    for i in range(m):
        u,v = map(int,input().split())
        if find(u) == find(v):
            return i+1

        _union(u, v)

    return 0

print(solution())