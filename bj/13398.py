n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp_remove = [0] * n
dp[0] = lst[0]
dp_remove[0] = lst[0]

for i in range(1,n):
    dp[i] = max(lst[i], dp[i-1]+lst[i])
    dp_remove[i] = max(dp_remove[i-1]+lst[i], dp[i-1])

print(max(dp+dp_remove))