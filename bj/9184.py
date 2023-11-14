dp = [[[-1]*21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a<b and b<c:
        ret = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        ret = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    
    dp[a][b][c] = ret
    return ret

while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1: break

    out = w(a,b,c)
    print(f'w({a}, {b}, {c}) = {out}')