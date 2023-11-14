import sys
input = sys.stdin.readline

bw = []
N,M,K = map(int, input().split())
for _ in range(N):
    row = list(input().strip())
    bw.append(row)


arr1 = [[0]*M for _ in range(N)]
arr2 = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0:
            arr1[i][j] = int(bw[i][j] == 'W')
            arr2[i][j] = arr1[i][j] ^ 1
        else:
            arr1[i][j] = int(bw[i][j] == 'B')
            arr2[i][j] = arr1[i][j] ^ 1

prefix1 = [[0]*(M+1) for _ in range(N+1)]
prefix2 = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        prefix1[i][j] = prefix1[i-1][j]+prefix1[i][j-1]-prefix1[i-1][j-1]+arr1[i-1][j-1]
        prefix2[i][j] = prefix2[i-1][j]+prefix2[i][j-1]-prefix2[i-1][j-1]+arr2[i-1][j-1]


answer = 1000000000
for i in range(K,N+1):
    for j in range(K,M+1):
        _sum1 = prefix1[i][j]+prefix1[i-K][j-K]-prefix1[i-K][j]-prefix1[i][j-K]
        _sum2 = prefix2[i][j]+prefix2[i-K][j-K]-prefix2[i-K][j]-prefix2[i][j-K]
        answer = min(answer,_sum1)
        answer = min(answer,_sum2)

print(answer)
