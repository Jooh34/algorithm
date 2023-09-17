def solution(matrix_sizes):
    mat = []
    for m in matrix_sizes:
        mat.append(m[0])
    mat.append(matrix_sizes[len(matrix_sizes)-1][1])

    dp = [[0] * len(mat) for _ in range(len(mat))]

    for n in range(2,len(mat)):
        for i in range(0, len(mat)-n):
            min_ = float('inf')
            for k in range(0, n-1):
                min_ = min(min_, dp[i][i+k+1]+dp[i+k+1][i+n] + mat[i]*mat[i+k+1]*mat[i+n])
            dp[i][i+n] = min_

    return dp[0][len(mat)-1]

q1 = [[5,3],[3,10],[10,6],[6,20],[20,10],[10,5]]
print(solution(q1))