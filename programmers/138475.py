def solution(e, starts):
    mem = [0]*(e+1)
    i=1
    while True:
        ni = i*i
        if ni > e: break

        mem[ni] -= 1
        while ni <= e:
            mem[ni] += 2
            ni += i
        
        i+=1
    
    dp = [0]*(e+1)

    mx = mem[e]
    dp[e] = e
    for i in range(e-1,-1,-1):
        if mx <= mem[i]:
            mx = mem[i]
            dp[i] = i
        else:
            dp[i] = dp[i+1]

    return [dp[s] for s in starts]

q = [8,	[1,3,7]]
print(solution(*q))