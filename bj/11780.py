import sys
input = sys.stdin.readline
INF = 1e9

def find_path(i,j):
    if trace[i][j] == -1:
        return []
    
    k = trace[i][j]
    return find_path(i,k) + [k] + find_path(k,j)

#floyd-warshall
n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
trace = [[-1] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int, input().split())
    if dist[u][v] > w:
        dist[u][v] = w

# initialize
for i in range(1,n+1):
    dist[i][i] = 0

for k in range(1,n+1): # pass through
    for i in range(1,n+1): # start point
        for j in range(1,n+1): # end point
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                trace[i][j] = k

for i in range(1,n+1):
    for j in range(1,n+1):
        print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
    print()
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == 0 or dist[i][j] == INF:
            print(0)
            continue
        else:
            path = [i] + find_path(i,j) + [j]
            print(len(path), end=' ')
            print(*path)