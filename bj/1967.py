#dfs
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    fr,to,cost = map(int, input().split())
    graph[fr].append((to,cost))
    graph[to].append((fr,cost))


def get_far_node(start):
    visited = [0]*(N+1)
    max_i = start
    max_v = 0
    q = [(start,0)] # index, cost

    while q:
        i,c = q.pop()
        if visited[i]:
            continue
        visited[i] = 1

        if max_v <= c:
            max_v = c
            max_i = i
        
        for to,cost in graph[i]:
            if not visited[to]:
                q.append((to, c+cost))

    return max_i,max_v

far_i, _ = get_far_node(1)
_, answer = get_far_node(far_i)
print(answer)
