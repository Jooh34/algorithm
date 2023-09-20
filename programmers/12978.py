from heapq import heappush, heappop
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for fr,to,co in road:
        graph[fr].append((to,co))
        graph[to].append((fr,co))

    answer = 0
    q = [(0,1)] #cost, index
    while q:
        cost, index = heappop(q)
        if visited[index]:
            continue

        visited[index]=True
        if cost <= K:
            answer += 1

        for next,next_cost in graph[index]:
            if not visited[next]:
                heappush(q, (cost+next_cost,next))
    
    return answer

q1 = [5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3]
print(solution(*q1))
