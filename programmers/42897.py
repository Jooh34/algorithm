def solution(money):
    one_zero = [0]*len(money)
    zero_one = [0]*len(money)
    zero_zero = [0]*len(money)
    one_one = [0]*len(money)

    one_zero[2] = money[0]
    zero_one[2] = money[2]
    zero_zero[2] = money[1]
    one_one[2] = money[0]+money[2]

    for i in range(3,len(money)):
        one_zero[i] = max(one_zero[i-1], one_one[i-1])
        zero_one[i] = zero_zero[i-1]+money[i]
        zero_zero[i] = max(zero_zero[i-1], zero_one[i-1])
        one_one[i] = one_zero[i-1]+money[i]
    
    answer = one_zero[len(money)-1]
    answer = max(answer, zero_one[len(money)-1])
    answer = max(answer, zero_zero[len(money)-1])

    return answer


q1 = [1, 6, 3, 4, 5, 10]
print(solution(q1))