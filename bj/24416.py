N = int(input())

def solve():
    if N == 0 or N == 1:
        return N
    
    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(2,N+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[N]

print(solve(), max(0,N-2))