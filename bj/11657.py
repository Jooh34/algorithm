INF = 1e9

N,M = map(int, input().split())

edges = []
dist = [INF for _ in range(N+1)]
dist[1]=0

for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

def bellman_ford():
    for i in range(N):
        for a,b,c in edges:
            if dist[a] != INF and dist[a]+c < dist[b]:
                dist[b] = dist[a]+c
                if i == N-1: # negative cycle exists when there's update on v'th round.
                    return True

    return False

neg_cycle = bellman_ford()
if neg_cycle:
    print(-1)
else:
    for i in range(2,N+1):
        d = dist[i]
        if d == INF:
            print(-1)
        else:
            print(d)
