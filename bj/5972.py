import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

dist = [-1]*(N+1)

q = [(0,1)] # cost, index
while q:
    c,i = heappop(q)
        
    if dist[i] != -1:
        continue
    dist[i] = c

    if i == N:
        break

    for next,next_c in graph[i]:
        if dist[next] == -1:
            heappush(q,(c+next_c,next))

print(dist[N])