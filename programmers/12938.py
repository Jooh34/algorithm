def solution(n, s):
    med = s // n
    rem = s % n
    if med == 0:
        return [-1]
    
    answer = [med]*n
    for i in range(n-1,n-1-rem,-1):
        answer[i] += 1

    return answer

ql = [[2,9],[2,1],[2,8],[3,10]]
for q in ql:
    print(solution(*q))