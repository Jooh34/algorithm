import sys
sys.setrecursionlimit(10**7)

def bfs(x,y,M,N):
    global visited, cell
    if visited[x][y]: return
    visited[x][y] = True
    if cell[x][y] == 0: return

    dir = [[-1,0], [1,0], [0,-1], [0,1]]
    for d in dir:
        if 0 <= x+d[0] < N and 0 <= y+d[1] < M:
            bfs(x+d[0], y+d[1], M, N)

def solution(M,N):
    global visited, cell
    visited = [[False] * M for _ in range(N)] 
    answer = 0

    for x in range(N):
        for y in range(M):
            if not visited[x][y] and cell[x][y] == 1:
                answer += 1
                bfs(x,y,M,N)
    
    print(answer)


n = int(sys.stdin.readline().strip())
for _ in range(n):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    global cell
    cell = [[0] * M for _ in range(N)]
    for _ in range(K):
        y,x = map(int, input().split())
        cell[x][y] = 1

    solution(M,N)
