import sys
input = sys.stdin.readline

MIN = -1e9
N,M = map(int,input().split())
b = []
for _ in range(N):
    row = list(map(int,input().split()))
    b.append(row)

dp_r = [[MIN]*M for _ in range(N)]
dp_l = [[MIN]*M for _ in range(N)]

dp_r[0][0] = b[0][0]
for j in range(1,M):
    dp_r[0][j] = dp_r[0][j-1] + b[0][j]

for i in range(1,N):
    up = []
    for j in range(M):
        up.append(max(dp_r[i-1][j], dp_l[i-1][j]))
    
    for j in range(M):
        if j == 0:
            dp_r[i][j] = up[j]+b[i][j]
        else:
            dp_r[i][j] = max(up[j], dp_r[i][j-1]) + b[i][j]

    for j in range(M-1,-1,-1):
        if j == M-1:
            dp_l[i][j] = up[j]+b[i][j]
        else:
            dp_l[i][j] = max(up[j], dp_l[i][j+1]) + b[i][j]

print(max(dp_r[N-1][M-1], dp_l[N-1][M-1]))