def solution(maps):
    m = len(maps)
    n = len(maps[0])
    v = [[False] * n for _ in range(m)]
    
    q = [[0,0,0]]
    dir = [[1,0], [-1,0], [0,1], [0,-1]]
    while q:
        x,y,d = q.pop(0)

        if v[x][y]: continue
        v[x][y] = True

        if x == m-1 and y == n-1:
            return d+1

        # bfs
        for di in dir:
            x_ = x+di[0]
            y_ = y+di[1]
            if 0 <= x_ < m and 0 <= y_ < n and maps[x_][y_] == 1:
                q.append([x_,y_,d+1])
    
    return -1

q1 = [[1,0,1,1,1],[1,0,1,1,1],[1,0,1,1,1],[1,1,1,0,1],[1,0,0,0,1]]
q2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(q1))
print(solution(q2))