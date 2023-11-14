from collections import deque

def solve():
    N = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    visited = [[0]*N for _ in range(N)]

    q = deque()
    q.append((sx,sy,0))
    while q:
        x,y,cnt = q.popleft()
        if visited[x][y]:
            continue
        
        if x==ex and y==ey:
            print(cnt)
            return

        visited[x][y] = 1

        dir_one = [-1,1]
        dir_two = [-2,2]
        for dx in dir_one:
            for dy in dir_two:
                nx = x+dx; ny = y+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        q.append((nx,ny,cnt+1))

        for dx in dir_two:
            for dy in dir_one:
                nx = x+dx; ny = y+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[nx][ny]:
                        q.append((nx,ny,cnt+1))
        

    pass

T = int(input())
for _ in range(T):
    solve()

