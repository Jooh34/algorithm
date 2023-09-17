from collections import deque
N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs = []
bfs = []

visited = [False]*(N+1)
q = [V]
while q:
    node = q.pop()
    if visited[node]:
        continue

    visited[node] = True
    dfs.append(node)

    for i in sorted(graph[node], reverse=True):
        if not visited[i]:
            q.append(i)

visited = [False]*(N+1)
q = deque([V])
while q:
    node = q.popleft()
    if visited[node]:
        continue

    visited[node] = True
    bfs.append(node)

    for i in sorted(graph[node]):
        if not visited[i]:
            q.append(i)

print(' '.join(map(str,dfs)))
print(' '.join(map(str,bfs)))