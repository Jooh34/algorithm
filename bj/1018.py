import sys
input = sys.stdin.readline 

N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(input().strip()))

min_ = 99999999
for start_i in range(len(board)-7):
    for start_j in range(len(board[0])-7):
        odd = 0
        even = 0
        for i in range(start_i, start_i+8):
            for j in range(start_j, start_j+8):
                if board[i][j] == 'W':
                    if (i+j) % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                else:
                    if (i+j) % 2 == 0:
                        odd += 1
                    else:
                        even += 1

        if min_ > min(even,odd):
            min_ = min(even,odd)

print(min_)