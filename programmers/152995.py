def solution(scores):
    wanho, scores = scores[0], scores[1:]
    wanho_a, wanho_b = wanho
    rank = 1
    last_b = 0
    for a,b in sorted(scores, key=lambda x: (-x[0], x[1])):
        if wanho_a < a and wanho_b < b:
            return -1

        if last_b <= b:
            last_b = b

            if wanho_a + wanho_b < a + b:
                rank += 1

    return rank

q = [[2,2],[1,4],[3,2],[3,2],[2,1]]
q2 = [[4, 0], [2, 5], [5, 3], [2, 6]]
print(solution(q))