from itertools import product
def solution(numbers, target):
    lenn = len(numbers)
    sign = [-1, 1]
    prods = list(product(sign, repeat=lenn))
    answer = 0

    for p in prods:
        sum = 0
        for i in range(lenn):
            sum += p[i]*numbers[i]
        
        if sum == target:
            answer+=1

    return answer

q1 = [[1, 1, 1, 1, 1], 3]
q2 = [[4, 1, 2, 1], 4]

print(solution(*q1))
print(solution(*q2))