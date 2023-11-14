N,M = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M,K = map(int, input().split())
B = []
for _ in range(M):
    row = list(map(int, input().split()))
    B.append(row)

C = [[0]*K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

for n in range(N):
    print(*C[n])