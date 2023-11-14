import sys
input = sys.stdin.readline
N,D = map(int,input().split())

shortcut = [[] for _ in range(10001)]
dp = [0]*(D+1)
for _ in range(N):
    a,b,c = map(int, input().split())
    shortcut[b].append((a,c))

for i in range(1,D+1):
    dp[i] = dp[i-1]+1
    for fr, cost in shortcut[i]:
        dp[i] = min(dp[i], dp[fr]+cost)

print(dp[D])
