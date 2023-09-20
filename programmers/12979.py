import math
def solution(n, stations, w):
    answer = 0
    stations.append(n+w+1)
    i=1
    for s in stations:
        start = s-w
        blank = start-i
        if blank > 0:
            answer += math.ceil(blank / (2*w+1))

        i= s+w+1

    # answer += math.ceil((n-i+1) / (2*w+1))

    return answer

q1 =[11,[4, 11],1]
q2 = [16,[9],2]
print(solution(*q1))
print(solution(*q2))