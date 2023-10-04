import math
def get_day(p, s):
    return math.ceil((100-p)/s)

def solution(progresses, speeds):
    answer = []

    days = []
    for p,s in zip(progresses,speeds):
        days.append(get_day(p,s))
    

    stck = 0
    distribution_day = 0
    for day in days:
        if distribution_day < day: # new
            if stck:
                answer.append(stck)
                stck = 0
            distribution_day = day
            stck=1
        
        else: # stck
            stck += 1

    answer.append(stck)
    return answer

q1 = [[93, 30, 55],[1, 30, 5]]
q2 = [[95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]]
print(solution(*q1))
print(solution(*q2))