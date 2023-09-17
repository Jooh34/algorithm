def solution(inp, max_):
    dp = [0]*(max_+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if max_ > 3:
        for n in range(4,max_+1):
            dp[n] = (dp[n-3]+dp[n-2]+dp[n-1])

    for i in inp:
        print(dp[i])

N = int(input())
max_ = 0
inp = []
for n in range(N):
    a = int(input())
    inp.append(a)
    if max_ < a:
        max_ = a

solution(inp,max_)