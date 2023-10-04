import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dp = [0] * (M+1) # weight -> max_value
lst = []
for _ in range(N):
    W, V, num = map(int,input().split())
    # divide item
    while num > 0:
        rem = num-(num>>1)
        lst.append((W*rem,V*rem))
        num-=rem

for W,V in lst:
    for w in range(M,-1,-1):
        if w >= W:
            dp[w] = max(dp[w], dp[w-W]+V)
                
print(dp[M])