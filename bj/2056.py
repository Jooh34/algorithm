import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
costs = [0]*(N+1)
for i in range(1,N+1):
    lst = list(map(int, input().split()))
    costs[i] = lst[0]
    for j in lst[2:]:
        graph[j].append(i)
        in_degree[i] += 1

pq = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        heappush(pq, (costs[i], i))

answer = 0
while pq:
    c,i = heappop(pq)
    answer = c

    for g in graph[i]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            heappush(pq, (costs[g]+c, g))

print(answer)