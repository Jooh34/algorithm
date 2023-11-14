import sys
input = sys.stdin.readline
from collections import deque


N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort()

visited = [0] * (N+1)
answer = [0] * (N+1)
cnt = 0



dfs(R)
for i in range(1,N+1):
    print(answer[i])