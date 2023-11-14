N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = [0] * (N+1)
q = [(1,1)] # index, parent
while q:
    i,p = q.pop()
    if parents[i]:
        continue
    parents[i] = p

    for g in graph[i]:
        q.append((g,i))

for i in range(2,N+1):
    print(parents[i])