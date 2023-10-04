def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
        
    l = len(sticker)
    dp1 = [-1]*l # 첫번째 스티커를 떼는 경우
    dp2 = [-1]*l # 첫번째 스티커를 떼지 않는 경우

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2,l-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    for i in range(2,l):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])

    return max(dp1[l-2], dp2[l-1])

q1 = [14, 6, 5, 11, 3, 9, 2, 10]
q2 = [1, 3, 2, 5, 4]
print(solution(q1))
print(solution(q2))