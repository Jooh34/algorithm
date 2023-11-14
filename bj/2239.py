N = 9

board = []
for _ in range(N):
    row = list(map(int, list(input())))
    board.append(row)

def print_board():
    for i in range(N):
        print(''.join(map(str,board[i])))

def check(i,j,x):
    for nj in range(N):
        if board[i][nj] == x:
            return False
    
    for ni in range(N):
        if board[ni][j] == x:
            return False
        
    start_i = (i//3)*3
    start_j = (j//3)*3
    
    for di in range(3):
        for dj in range(3):
            if board[start_i+di][start_j+dj] == x:
                return False

    return True

def btk(ij):
    if ij == 81:
        print_board()
        exit(0)
    i = ij // N
    j = ij % N

    if board[i][j] != 0:
        btk(ij+1)
    else:
        for x in range(1,N+1):
            b = check(i,j,x)
            if b:
                board[i][j] = x
                btk(ij+1)
                board[i][j] = 0

btk(0)
