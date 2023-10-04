import sys
input = sys.stdin.readline

N,K = map(int,input().split())
dp = [0] * (K+1) # weight -> max_value

for _ in range(N):
    W, V = map(int,input().split())
    for w in range(K,-1,-1):
        if w >= W:
            dp[w] = max(dp[w], dp[w-W]+V)

print(dp[K])