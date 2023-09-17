def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    for w,l in results:
        graph[w][l] = 1
        graph[l][w] = -1

    answer = 0
    # check all person
    for n_ in range(n+1):
        q = [n_]
        
        # traverse loser
        visited = set()
        while q:
            i = q.pop(0)
            visited.add(i)
            for j in range(n+1):
                if graph[i][j] == 1:
                    if not j in visited: q.append(j)

        # traverse winner
        q = [n_]
        while q:
            i = q.pop(0)
            visited.add(i)
            for j in range(n+1):
                if graph[i][j] == -1:
                    if not j in visited: q.append(j)

        # check judgable
        if len(visited) == n:
            answer += 1

    return answer


q1 = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(5, q1))