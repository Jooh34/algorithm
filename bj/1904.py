N = int(input())

def solve():
    if N == 1 or N == 2:
        return N
    dp = [0]*(N+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,N+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 15746

    return dp[N]

print(solve())