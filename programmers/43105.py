def solution(triangle):
    h = len(triangle)

    for i in range(h-2,-1,-1):
        for j in range(i+1):
            bigger = triangle[i+1][j+1] if triangle[i+1][j] < triangle[i+1][j+1] else triangle[i+1][j]
            triangle[i][j] += bigger

    return triangle[0][0]


q1 = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(q1))