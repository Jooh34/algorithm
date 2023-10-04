#Dijkstra
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N,M,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
for _ in range(M):
    fr,to,cost = map(int, input().split())
    graph[fr].append((to,cost))
    reverse_graph[to].append((fr,cost))

def dfs(start, in_graph):
    distance = [-1]*(N+1)
    q = [(0, start)] # cost, index

    while q:
        c,i = heappop(q)
        if distance[i] != -1:
            continue
        distance[i] = c
        
        for to,cost in in_graph[i]:
            if distance[to] == -1:
                heappush(q, (c+cost, to))

    return distance

dist = dfs(X, graph)
reversed_dist = dfs(X, reverse_graph)

sum_list = [x+y for x,y, in zip(dist,reversed_dist)]
print(max(sum_list[1:]))
