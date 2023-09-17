import sys
input = sys.stdin.readline 
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0

visited = [False]*(N+1)
for i in range(1,N+1):
    if visited[i]:
        continue

    q = [i]
    while q:
        node = q.pop()
        if visited[node]:
            continue

        visited[node] = True

        for i in graph[node]:
            if not visited[i]:
                q.append(i)

    answer+=1

print(answer)