
def subproblem(n, weak, dist):
    min_ = 99999999
    if not weak: # cleaned all
        return 0
    
    if not dist: # impossible
        return min_

    d = dist[0]
    for i in range(len(weak)):
        new_i = (i+len(weak)+1) % len(weak)
        while new_i != i:
            use_d = (weak[new_i] - weak[i] + n) % n
            if d < use_d:
                break
            
            new_i = (new_i+len(weak)+1) % len(weak)
        
        print(d, i, new_i, weak)
        if i < new_i:
            new_weak = weak[:i] + weak[new_i:]
        elif i > new_i:
            new_weak = weak[new_i:i]
        else: # new_weak = 0
            min_ = min(min_, 1)
            continue

        min_ = min(min_, subproblem(n, new_weak, dist[1:])+1)

    return min_

def solution(n, weak, dist):
    answer = 0
    dist = sorted(dist, reverse=True)

    answer = subproblem(n, weak, dist)
    if answer > 90000000:
        return -1
    return answer

q1 = [12, [1, 5, 6, 10], [1, 2, 3, 4]]
q2 = [12, [1, 3, 4, 9, 10], [3, 5, 7]]
print(solution(*q1))