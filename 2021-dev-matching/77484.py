def solution(lottos, win_nums):
    win = 0
    blank = 0
    for l in lottos:
        if l in win_nums:
            win+=1
        if l == 0:
            blank+=1

    max_ = min(7-(win+blank),6)
    min_ = min(7-win, 6)
    answer = [max_,min_]
    return answer

q1= [[44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]]
q2 = [[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]]
print(solution(*q1))