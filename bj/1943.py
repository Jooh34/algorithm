def solve():
    n = int(input())
    sum_ = 0
    coins = []
    for _ in range(n):
        m,n = map(int, input().split())
        sum_+= m*n
        i = n
        while i >> 1 != 0:
            x = i >> 1
            coins.append(m*x)
            i -= x
        
        coins.append(m*i)
    
    if sum_ % 2 == 1:
        return 0

    half = sum_ // 2
    dp = [0] * (half+1)
    dp[0] = 1
    
    for c in sorted(coins):
        for i in range(half, c-1, -1):
            dp[i] += dp[i-c]

    return 1 if dp[half] else 0

for _ in range(3):
    print(solve())
