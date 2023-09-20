import sys
input = sys.stdin.readline
from collections import deque


N,K = map(int,input().split())
dp = [-1] * (K+1) # weight -> value
dp[0] = 0
max_ = 0

for _ in range(N):
    W, V = map(int,input().split())
    for w in range(K,-1,-1):
        if dp[w] == -1:
            continue
        new_weight = w+W
        if new_weight <= K:
            new_value = dp[w]+V
            if new_value > dp[new_weight]:
                dp[new_weight] = new_value
                if max_ < new_value:
                    max_ = new_value

print(max_)
