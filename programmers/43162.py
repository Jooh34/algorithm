def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer += 1
            traverse(i, computers, visited)


    return answer

def traverse(i, computers, visited):
    for j, conn in enumerate(computers[i]):
        if conn == 1 and not visited[j] :
            visited[j] = True
            traverse(j, computers, visited)

q1 = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

q2 = [
    [1,1,0],
    [1,1,1],
    [0,1,1]
]

print(solution(3, q1))
print(solution(3, q2))