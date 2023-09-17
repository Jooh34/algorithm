def solution(gems):
    # find gem kind
    kinds = set(gems)
    num_kind = len(kinds)
    len_gems = len(gems)
    min = 99999999
    answer = 0

    # do find
    start = 0
    end = -1
    d = dict()

    while start < len_gems and end < len_gems:
        # find all kind
        if len(d) == num_kind:
            distance = end-start
            # print(f'find! dist{distance} start{start}, end{end}')
            if distance < min:
                min = distance
                answer = start
        
            # delete first gem
            delete_g = gems[start]
            start += 1
            if d[delete_g] == 1:
                del d[delete_g]
            else:
                d[delete_g] = d[delete_g] - 1
        
        else:
            end+=1
            if end == len_gems : break
            g = gems[end]
            if d.get(g):
                d[g] += 1
            else:
                d[g] =1
            
    answer = [answer+1, answer+min+1]
    return answer



q1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
q2 = ["AA", "AB", "AC", "AA", "AC"]
q3 = ["XYZ", "XYZ", "XYZ"]
q4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
q5 = ["A", "A", "A", "C", "C", "C"]

print(solution(q1))
print(solution(q2))
print(solution(q3))
print(solution(q4))
print(solution(q5))