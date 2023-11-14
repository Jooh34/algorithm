from heapq import heappush, heappop

INF = 1e9

def solve():
    N,M,T = map(int, input().split())
    S,G,H = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v,c = map(int, input().split())
        graph[u].append((v,c))
        graph[v].append((u,c))

    targets = [0]*(N+1)
    for _ in range(T):
        x = int(input())
        targets[x] = 1

    def dij(s):
        answers = [0]*(N+1)
        dist = [INF]*(N+1)
        use_gh = [0]*(N+1)

        q = [(0, s, 0)] # cost, index, pass-gh
        dist[s] = 0
        use_gh[s] = 0

        while q:
            c,i,p = heappop(q)
            if dist[i] < c:
                continue

            if targets[i] and p:
                answers[i] = 1
            
            for next,cost in graph[i]:
                next_cost = c+cost
                next_p = p
                if (i==G and next==H) or (i==H and next==G):
                    next_p = 1

                if dist[next] > next_cost:
                    dist[next] = next_cost
                    use_gh[next] = next_p
                    heappush(q, (next_cost, next, next_p))

                elif dist[next] == next_cost:
                    if use_gh[next] == 0 and next_p == 1:
                        use_gh[next] = next_p
                        heappush(q, (next_cost, next, next_p))


        return answers

    ret = dij(S)

    answers = []
    for i,r in enumerate(ret):
        if r == 1:
            answers.append(i)

    print(*answers)

TC = int(input())
for _ in range(TC):
    solve()