from collections import deque
import sys

def solution(M,N,cell):
    global visited
    visited = [[False] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and cell[i][j] == 1:
                answer += 1

            q = deque([[i,j]])
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y]=True

                if cell[x][y] == 0: continue
                if x-1 >= 0:
                    q.append([x-1,y])
                if y-1 >= 0:
                    q.append([x,y-1])
                if x+1 < N:
                    q.append([x+1,y])
                if y+1 < M:
                    q.append([x,y+1])
    
    print(answer)


n = int(sys.stdin.readline().strip())
for _ in range(n):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    cell = [[0] * M for _ in range(N)]
    for _ in range(K):
        y,x = map(int, input().split())
        cell[x][y] = 1
    solution(M,N,cell)
