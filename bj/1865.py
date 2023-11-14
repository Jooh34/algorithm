T = int(input())
INF = 1e9

for _ in range(T):
    edges = []
    N,M,W = map(int, input().split())
    for _ in range(M):
        a,b,c = map(int, input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))

    for _ in range(W):
        a,b,c = map(int, input().split())
        edges.append((a,b,-c))


    def bellman_ford(dist):
        for i in range(N):
            for a,b,c in edges:
                if dist[a] != INF and dist[a]+c < dist[b]:
                    dist[b] = dist[a]+c
                    if i == N-1: # negative cycle exists when there's update on last round.
                        return True

        return False

    dist = [INF for _ in range(N+1)]
    neg = False
    for n in range(1,N+1):
        if dist[n] != INF:
            continue
        dist[n]=0
        neg_cycle = bellman_ford(dist)
        if neg_cycle:
            print("YES")
            neg = True
            break
    
    if not neg:
        print("NO")