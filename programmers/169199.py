from collections import deque

def solution(board):
    queue = deque([])
    len_board_y = len(board)
    len_board_x = len(board[0])
    visited = [[-1] * len_board_x for i in range(len_board_y)]

    # make board
    b = []
    for y in range(len_board_y):
        s = list(board[y])
        b.append(s)
        for x, ch in enumerate(s):
            if ch == 'R':
                queue.append([y,x,0])


    while queue:
        node = queue.popleft()
        y,x,n = node

        # skip visited
        if visited[y][x] != -1:
            continue

        visited[y][x] = 1

        # goal
        if b[y][x] == 'G':
            return n

        # bfs
        x_=x
        while 0 <= x_:
            ch = b[y][x_]
            if ch == 'D':
                break

            x_-=1
        
        if visited[y][x_+1] == -1: queue.append([y,x_+1,n+1])

        x_=x
        while x_ < len_board_x:
            ch = b[y][x_]
            if ch == 'D':
                break

            x_+=1
        if visited[y][x_-1] == -1: queue.append([y,x_-1,n+1])

        y_=y
        while 0 <= y_:
            ch = b[y_][x]
            if ch == 'D':
                break

            y_-=1
        if visited[y_+1][x] == -1: queue.append([y_+1, x,n+1])

        y_=y
        while y_ < len_board_y:
            ch = b[y_][x]
            if ch == 'D':
                break

            y_+=1
        if visited[y_-1][x] == -1: queue.append([y_-1, x,n+1])
    
    return -1


q1 = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
q2 = [".D.R", "....", ".G..", "...D"]

print(solution(q1))
print(solution(q2))