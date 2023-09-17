def solution(routes):
    sor = sorted(routes, key=lambda x: x[1])
    last = -30001
    answer = 0
    for s in sor:
        if s[0] <= last:
            continue
        else: # new camera
            answer+=1
            last = s[1]

    return answer


q1 = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(q1))