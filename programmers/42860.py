def solution(name):
    l = len(name)
    answer = 0

    vals = []
    for ch in name:
        v = ord(ch)-ord('A')
        if v > 13:
            v = 26-v
        vals.append(v)
    
    answer += sum(vals)
    # make distance array
    dists = []

    dist = 1
    for v in vals[1:]:
        if v != 0:
            dists.append(dist)
            dist = 1
        else:
            dist += 1

    dists.append(dist)

    if len(dists) == 1:
        return answer

    minval = 99999999
    for i in range(len(dists)):
        a = sum(dists[:i])
        b = sum(dists[i+1:])
        mov = 0
        if a < b:
            mov = 2*a+b
        else:
            mov = a+(2*b)

        if minval > mov:
            minval = mov

    return answer + minval

q1 = "JEROENA"
q2 = "JAN"
q3 = "AAA"
q4 = "ABAA"
print(solution(q1))
print(solution(q2))
print(solution(q3))
print(solution(q4))