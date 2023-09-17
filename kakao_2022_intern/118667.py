from collections import deque

def solution(queue1, queue2):
    answer = 0
    target_sum = (sum(queue1) + sum(queue2))
    d1 = deque(queue1)
    d2 = deque(queue2)
    if target_sum % 2 == 1:
        return -1
    max_move = (len(queue1) + len(queue2)) * 4

    sum1 = sum(d1)
    sum2 = sum(d2)
    while sum1 != sum2 and d1 and d2 and answer < max_move:
        if sum1 < sum2:
            a = d2.popleft()
            d1.append(a)
            sum1 += a
            sum2 -= a
        else:
            a = d1.popleft()
            d2.append(a)
            sum2 += a
            sum1 -= a

        answer+=1

    if sum1 == sum2: return answer
    else: return -1

q1 = [[3, 5], [9, 13]]
print(solution(*q1))