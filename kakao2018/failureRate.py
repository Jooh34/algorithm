def solution(N, stages):
    answer = []
    current = [0] * (N + 1)
    stack = [0] * (N + 1)

    for stage in stages:
        current[stage-1] += 1
        for i in range(stage):
            stack[i] += 1

    rate = []
    for i in range(N):
        if stack[i] == 0:
            rate.append([i,0])
        else:
            rate.append([i, current[i] / stack[i]])

    rate = sorted(rate, key=lambda r: r[1], reverse=True)
    for r in rate:
        answer.append(r[0]+1)

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
