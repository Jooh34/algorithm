import sys
input = sys.stdin.readline
INF = 1e9
#floyd-warshall
n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]
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
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1,n+1):
    lst = dist[i][1:]
    answer = []
    for el in lst:
        if el == INF:
            answer.append(0)
        else:
            answer.append(el)
    
    print(*answer)