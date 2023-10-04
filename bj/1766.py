from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
for _ in range(M):
    fr, to = map(int, input().split())
    graph[fr].append(to)
    in_degree[to] += 1

hq = []
# add root node
for i in range(1, N+1):
    if in_degree[i] == 0:
        heappush(hq, i)

answer = []
while hq:
    node = heappop(hq)
    answer.append(node)

    for g in graph[node]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            heappush(hq, g)

print(*answer)