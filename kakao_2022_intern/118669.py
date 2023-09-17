from collections import defaultdict
from heapq import heappush, heappop

MAX = 99999999
def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for fr, to, cost in paths:
        graph[fr].append((to,cost))
        graph[to].append((fr,cost))

    info = [0] * 50000
    for g in gates: info[g] = 1
    for s in summits: info[s] = 2
    
    dp = [MAX] * 50000
    answer = [50000, MAX]
    q = [(0,g) for g in gates] # (intensity, node)

    while q:
        inten, node = heappop(q)
        if answer[1] < inten : continue

        if info[node] == 2: # summit, multiple summit possible. find min
            if answer[0] > node:
                answer = [node, inten]
            continue
        
        for to, cost in graph[node]:
            if info[to] != 1 : # never go to gate
                new_inten = max(cost,inten)
                if dp[to] <= new_inten:
                    continue

                dp[to] = new_inten
                heappush(q, (new_inten, to))

    return answer


q1 = [6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5]]
q2 = [7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1],	[2, 3, 4]]
q3 = [7,	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7],	[1, 5]]
q4 = [5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],[1, 2],	[5]]
for q in [q1,q2,q3,q4]:
    print(solution(*q))