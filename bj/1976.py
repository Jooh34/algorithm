import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

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

for i in range(1,N+1):
    row = list(map(int,input().split()))
    for j_ in range(0,N):
        if row[j_] == 1:
            union_(i,j_+1)

tour = list(map(int,input().split()))

answer = "YES"
value = find(tour[0])
for t in tour:
    if find(t) != value:
        answer = "NO"
        break

print(answer)
