from collections import defaultdict
def solution(survey, choices):
    cho = defaultdict(int)
    for s,c in zip(survey,choices):
        one,two = s[0],s[1]
        if c < 4:
            cho[one] += (4-c)
        elif c > 4:
            cho[two] += (c-4)
    
    answer = ''
    li = [['R','T'], ['C','F'], ['J', 'M'], ['A', 'N']]
    for a,b in li:
        if cho[a] < cho[b]: answer += b
        else: answer += a

    return answer

q1 = [["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]	]
q2 = [["TR", "RT", "TR"], [7, 1, 3]	]
print(solution(*q1))
print(solution(*q2))