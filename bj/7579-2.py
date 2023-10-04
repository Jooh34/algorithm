import sys
input = sys.stdin.readline

N,M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split())) 
sum_cost = sum(costs)

dp = [0]*(sum_cost+1) # dp[i] : max memory with i cost.

def solution():
    for i in range(N):
        for j in range(sum_cost,-1,-1):
            if j-costs[i] >= 0:
                dp[j] = max(dp[j], dp[j-costs[i]]+mems[i]) # select i'th app 

    for j in range((sum_cost+1)):
        if dp[j] >= M:
            return j

print(solution())