import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
for _ in range(M):
    lst = list(map(int, input().split()))[1:]
    for i in range(len(lst)-1):
        graph[lst[i]].append(lst[i+1])
        in_degree[lst[i+1]] += 1

q = []
# add root node
for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

answer = []
while q:
    node = q.pop()
    answer.append(node)

    for g in graph[node]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            q.append(g)

if len(answer) == N:
    print(*answer)
else:
    print(0)