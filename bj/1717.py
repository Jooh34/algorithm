import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union_(x,y):
    px = find(x)
    py = find(y)
    
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

for _ in range(m):
    comm, a, b = map(int, input().split())
    if comm == 0:
        union_(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
