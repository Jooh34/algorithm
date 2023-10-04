import sys
input = sys.stdin.readline
# TSP
INF = int(1e9)
n = int(input())
W = []
dp = [[-1] * ((1<<n)-1) for _ in range(n)] # cur, bitmask
for _ in range(n):
    row = list(map(int, input().split()))
    W.append(row)

def dfs(x, visited):
    if visited == (1<<n)-1: # visited all cities
        if W[x][0]:
            return W[x][0]
        else:
            return INF
    
    if dp[x][visited] != -1:
        return dp[x][visited]
    dp[x][visited] = INF

    for i in range(1,n):
        if visited & (1 << i): # already visited
            continue
        if W[x][i] == 0:
            continue
        
        new_v = W[x][i]+dfs(i, visited | (1 << i))
        dp[x][visited] = min(dp[x][visited], new_v)

    return dp[x][visited]

print(dfs(0,1))