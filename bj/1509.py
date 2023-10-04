s = input()
N = len(s)
palin = [[False]*N for _ in range(N)]
dp = [0]*(N+1) # 0~i 까지 최소

for i in range(N):
    palin[i][i] = True

for i in range(N-1):
    palin[i][i+1] = s[i] == s[i+1]

for j in range(2,N):
    for i in range(N-j): # i+j < N
        palin[i][i+j] = palin[i+1][i+j-1] and (s[i] == s[i+j])

dp[-1] = 0
for i in range(N):
    dp[i] = 1e9
    for j in range(i+1):
        if palin[j][i]:
            dp[i] = min(dp[i], dp[j-1]+1)

print(dp[N-1])