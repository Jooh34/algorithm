from heapq import heappush, heappop
import sys
input = sys.stdin.readline

#kruskal algorithm
N = int(input())
xlst = []
ylst = []
zlst = []
edges = []
for i in range(N):
    x,y,z = list(map(int, input().split()))
    xlst.append((x,i))
    ylst.append((y,i))
    zlst.append((z,i))

xlst.sort()
ylst.sort()
zlst.sort()
for i in range(N-1):
    edges.append((xlst[i+1][0]-xlst[i][0], xlst[i][1], xlst[i+1][1]))
    edges.append((ylst[i+1][0]-ylst[i][0], ylst[i][1], ylst[i+1][1]))
    edges.append((zlst[i+1][0]-zlst[i][0], zlst[i][1], zlst[i+1][1]))

edges.sort(key=lambda x:x[0]) # (cost, p1, p2)

parent = [i for i in range(N)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])

    return parent[u]

def union_(u, v):
    pu = find(u)
    pv = find(v)
    if pu < pv:
        parent[pu] = pv
    else:
        parent[pv] = pu

answer = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union_(a, b)
        answer += cost

print(answer)
