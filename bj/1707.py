T = int(input())

def solve():
    V,E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0]*(V+1)
    for i in range(1,V+1):
        if visited[i]:
            continue

        q = []
        q.append((i,1))
        while q:
            n, color = q.pop()
            visited[n] = color
            for g in graph[n]:
                if visited[g] == 0:
                    q.append((g,-color))
                elif visited[n] == visited[g]:
                    return False

    return True

for _ in range(T):
    p = solve()
    if p:
        print("YES")
    else:
        print("NO")