N,B = map(int, input().split())
mat = []
for _ in range(N):
    row = list(map(int, input().split()))
    mat.append(row)

dp_v = [0]*40
dp = [[[0]*N for _ in range(N)] for _ in range(40)] # 40 x N x N

dp_v[0]=1
dp[0]=mat

answer = [[0]*N for _ in range(N)]
for i in range(N):
    answer[i][i]=1

def matmul(a,b):
    ret = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += a[i][k] * b[k][j]
            
            ret[i][j] %= 1000
    return ret

def matpow(i):
    if dp_v[i]:
        return dp[i]
    else:
        ret = matmul(matpow(i-1),matpow(i-1))
        dp_v[i] = 1
        dp[i] = ret
        return ret

while B:
    i = 0
    while True:
        if B < (1 << (i+1)):
            break
        i+=1

    answer = matmul(answer, matpow(i))
    B -= (1 << i)

for i in range(N):
    print(*answer[i])