def check(rocks, n, val):
    remove = 0
    prev = 0
    for r in rocks:
        if r - prev < val: # remove rock
            remove += 1
            if remove > n: return False # fail
        
        else: # pass rock
            prev = r

    return True

def solution(distance, rocks, n):
    rocks = sorted(rocks) + [distance]
    answer = 0

    start = 1
    end = distance+1
    while start < end:
        mid = (start+end) // 2

        if check(rocks, n, mid):
            answer = mid
            start = mid+1
        else:
            end = mid

    return answer


q1 = [25, [2, 14, 11, 21, 17], 2]
q2 = [3, [1,2], 1]
print(solution(*q1))
print(solution(*q2))