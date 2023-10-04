from collections import deque
INF = 1e9

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for f,t in roads:
        graph[f].append(t)
        graph[t].append(f)
    
    dist = [INF] * (n+1)
    # BFS
    q = deque([(destination, 0)]) # index, cost
    while q:
        i,c = q.popleft()
        if dist[i] > c:
            dist[i] = c
            
        for g in graph[i]:
            if dist[g] > c+1:
                q.append((g,c+1))

    answer = list(map(lambda x: dist[x] if dist[x] != INF else -1, sources))

    return answer

q1 = [3,[[1, 2], [2, 3]],[2, 3],1]
q2 = [5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1, 3, 5],	5]
print(solution(*q1))
print(solution(*q2))