N, M = map(int,input().split())

graph = [[] for _ in range(N)]
for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i, s):
    if len(s) >= 5:
        return 1

    answer = 0
    for g in graph[i]:
        if g in s:
            continue

        s.add(g)
        answer += dfs(g, s)
        s.remove(g)
    
    return answer

def solution():
    for i in range(N):
        a = dfs(i, set([i]))
        if a >= 1:
            return 1

    return 0

print(solution())
