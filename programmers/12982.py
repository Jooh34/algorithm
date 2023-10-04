def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if i <= budget:
            answer += 1
            budget-=i
        else:
            break
    return answer

q1 = [[1,3,2,5,4],9]
print(solution(*q1))