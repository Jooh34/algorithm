def solution(dirs):
    board_up = [[0] * 15 for _ in range(15)]
    board_right = [[0] * 15 for _ in range(15)]
    answer = 0

    pos = (0,0)
    for s in list(dirs):
        if s=='U' and -5 <= pos[0] <= 5 and -5 <= pos[1]+1 <= 5:
            if board_up[pos[0]][pos[1]] == 0:
                answer += 1
            board_up[pos[0]][pos[1]] = 1
            pos = (pos[0], pos[1]+1)
        elif s=='D' and -5 <= pos[0] <= 5 and -5 <= pos[1]-1 <= 5:
            if board_up[pos[0]][pos[1]-1] == 0:
                answer += 1
            board_up[pos[0]][pos[1]-1] = 1
            pos = (pos[0], pos[1]-1)
        elif s=='R' and -5 <= pos[0]+1 <= 5 and -5 <= pos[1] <= 5:
            if board_right[pos[0]][pos[1]] == 0:
                answer += 1
            board_right[pos[0]][pos[1]] = 1
            pos = (pos[0]+1, pos[1])
        elif s=='L' and -5 <= pos[0]-1 <= 5 and -5 <= pos[1] <= 5:
            if board_right[pos[0]-1][pos[1]] == 0:
                answer += 1
            board_right[pos[0]-1][pos[1]] = 1
            pos = (pos[0]-1, pos[1])

    return answer

ql = ["ULURRDLLU", "LULLLLLLU"]
for q in ql:
    print(solution(q))