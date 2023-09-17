from collections import defaultdict

def solution(n, edge):
    #make graph
    conn = [[]] * n
    for f,t in edge:
        conn[f-1] = conn[f-1] + [t-1]
        conn[t-1] = conn[t-1] + [f-1]

    count = defaultdict(int)
    visited = [False]*n
    max_d = 0

    q = [[0, 0]] # (index, distance) 
    while q:
        node, d = q.pop(0)
        if visited[node]: continue
        visited[node] = True

        count[d] += 1
        max_d = d

        for i in conn[node]:
            if not visited[i]:
                q.append([i, d+1])

    return count[max_d]


q1 = [6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]]
q2 = [3,[[1, 2], [2, 3], [1, 3]]]
print(solution(*q1))
print(solution(*q2))