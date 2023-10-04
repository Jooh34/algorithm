import sys
input = sys.stdin.readline

N,M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split())) 
sum_cost = sum(costs)

dp = [[0]*(sum_cost+1) for _ in range(N)] # dp[i][j] : until i'th, j cost.

def solution():
    for i in range(N):
        for c in range(sum_cost+1):
            if c-costs[i] >= 0:
                dp[i][c] = max(dp[i][c], dp[i-1][c-costs[i]] + mems[i]) # select i'th app 
            
            dp[i][c] = max(dp[i][c], dp[i-1][c]) # don't select i'th app

            if i == N-1 and dp[i][c] >= M:
                return c

print(solution())