def solution(sequence):
    cusum = [0]
    for i in range(len(sequence)):
        cusum.append(cusum[i] + sequence[i] * (-1)**i)
    
    answer = abs(max(cusum) - min(cusum))
    return answer

q1 = [2, 3, -6, 1, 3, -1, 2, 4]
print(solution(q1))