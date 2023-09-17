from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 101
    board = [[0]*MAX for _ in range(MAX)]
    rectangle = [[2*x for x in r] for r in rectangle]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    for x1,y1,x2,y2 in rectangle:
        for y in range(y1,y2+1):
            board[x1][y] = 1
            board[x2][y] = 1
        for x in range(x1,x2+1):
            board[x][y1] = 1
            board[x][y2] = 1
    
    for x1,y1,x2,y2 in rectangle:
        for y in range(y1+1,y2):
            for x in range(x1+1, x2):
                board[x][y] = 0
                board[x][y] = 0
    
    # bfs
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    q = deque([(characterX, characterY, 0)])
    while q:
        x,y,c = q.popleft()
        if x==itemX and y==itemY:
            return c // 2

        board[x][y] = 0
        for dx,dy in dirs:
            if 0 <= x+dx < MAX and 0 <= y+dy < MAX and board[x+dx][y+dy] == 1:
                q.append([x+dx,y+dy,c+1])

q1 = [[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8]
print(solution(*q1))