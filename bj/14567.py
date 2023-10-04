import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

q = deque([])
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append((i, 1))

answer = [0 for _ in range(N+1)]
while q:
    i, cnt = q.popleft()
    answer[i] = cnt

    for g in graph[i]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            q.append((g, cnt+1))

print(*answer[1:])