N = int(input())
glasses = list(map(int, input().split()))
sum_g = sum(glasses)
M = int(input())
targets = list(map(int, input().split()))

dp = [0]*(2*sum_g+1)
dp[0] = 1
for glass in glasses:
    for i in range(sum_g,-sum_g-1,-1):
        if i-glass >= -sum_g:
            dp[i] = max(dp[i],dp[i-glass])
    for i in range(-sum_g, sum_g+1):
        if i+glass <= sum_g:
            dp[i] = max(dp[i], dp[i+glass])

answer = []
for t in targets:
    if sum_g < t:
        answer.append('N')   
    else:
        if dp[t]:
            answer.append('Y')
        else:
            answer.append('N')

print(*answer)