import sys
input = sys.stdin.readline

def solution(mat):
    N = len(mat)
    dp = [[0] * N for _ in range(N)]
    
    for j in range(2,N):
        for i in range(0, N-j): # i+j < N
            dp[i][i+j] = 1e9
            for k in range(1, j):
                dp[i][i+j] = min(dp[i][i+j], dp[i][i+k]+dp[i+k][i+j] + mat[i]*mat[i+k]*mat[i+j])

    return dp[0][N-1]

N = int(input())
mat = []
for i in range(N):
    a,b = list(map(int, input().split()))
    mat.append(a)
    if i == N-1:
        mat.append(b)
print(solution(mat))