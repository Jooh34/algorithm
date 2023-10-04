from collections import defaultdict
def solution(clothes):
    d = defaultdict(int)
    for _, ty in clothes:
        d[ty] += 1

    answer = 1
    for k in d:
        answer *= (d[k]+1) 

    return answer-1

q = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(q))