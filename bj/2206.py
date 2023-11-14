import sys
input = sys.stdin.readline
from collections import deque

def solve():
    N,M = map(int, input().split())
    b = []
    for _ in range(N):
        row = list(map(int, list(input().strip())))
        b.append(row)

    visited = [[[0]*M for _ in range(N)], [[0]*M for _ in range(N)]] # not_used, used

    q = deque([(0,0,1,0)]) #i,j,cost,used
    while q:
        i,j,c,used = q.popleft()
        if visited[used][i][j]:
            continue

        visited[used][i][j] = 1

        if i == N-1 and j == M-1:
            return c

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for dx,dy in dirs:
            xx = i+dx
            yy = j+dy
            if 0 <= xx < N and 0 <= yy < M:
                if b[xx][yy] == 0:
                    if visited[used][xx][yy] == 0:
                        q.append((xx,yy,c+1,used))
                else:
                    if used == False and visited[True][xx][yy] == 0:
                        q.append((xx,yy,c+1,True))
    
    return -1

print(solve())