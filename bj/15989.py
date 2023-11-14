T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

m = max(lst)
dp = [1]*(m+1)

for i in range(2,m+1):
    dp[i] += dp[i-2]

for i in range(3,m+1):
    dp[i] += dp[i-3]

for el in lst:
    print(dp[el])