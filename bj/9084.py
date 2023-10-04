import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    coins = [int(x) for x in input().split()]
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1

    for c in coins:
        for j in range(c,M+1):
            dp[j] += dp[j-c]

    return dp[M]

T = int(input())
for _ in range(T):
    print(solution())
