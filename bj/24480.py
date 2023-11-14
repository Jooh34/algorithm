import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)
answer = [0] * (N+1)
global cnt
cnt = 0
def dfs(r):
    global cnt
    cnt += 1
    visited[r] = 1
    answer[r] = cnt
    
    for g in graph[r]:
        if visited[g] == 0:
            dfs(g)

dfs(R)
for i in range(1,N+1):
    print(answer[i])