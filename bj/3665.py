import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    M = int(input())

    graph = [[False]*(N+1) for _ in range(N+1)]
    in_degree = [0 for _ in range(N+1)]
    
    for i in range(N):
        for j in range(i+1,N):
            graph[lst[i]][lst[j]] = True
            in_degree[lst[j]] += 1

    for _ in range(M):
        u,v = map(int, input().split())
        if graph[u][v] == True:
            in_degree[u]+=1
            in_degree[v]-=1
        
        if graph[v][u] == True:
            in_degree[v]+=1
            in_degree[u]-=1
        
        graph[u][v] = not graph[u][v]
        graph[v][u] = not graph[v][u]

    q = []
    # add root node
    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)

    answer = []
    while q:
        node = q.pop()
        answer.append(node)

        for i,conn in enumerate(graph[node]):
            if i == 0:
                continue
            if conn:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)

    if len(answer) == N:
        print(*answer)
    else:
        print("IMPOSSIBLE")