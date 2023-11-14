import sys
input = sys.stdin.readline

def solve():
    F = int(input())
    parent = {}
    num_table = {}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union_(x,y):
        if x == y:
            return

        px = find(x)
        py = find(y)
        
        if px < py:
            parent[py] = px
            num_table[px] = num_table[px] + num_table[py]
        elif px > py:
            parent[px] = py
            num_table[py] = num_table[px] + num_table[py]
        else:
            return

    for _ in range(F):
        a,b = input().split()
        if not parent.get(a):
            parent[a] = a
            num_table[a] = 1
        if not parent.get(b):
            parent[b] = b
            num_table[b] = 1
        
        union_(a,b)
        print(num_table[find(a)])

T = int(input())
for _ in range(T):
    solve()