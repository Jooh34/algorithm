from collections import deque

N, M = map(int, input().split())

def solve():
    jump = {}
    for _ in range(N+M):
        f,t = map(int, input().split())
        jump[f] = t

    visited = [0]*101
    q = deque()
    q.append((1,0))
    while q:
        n,cnt = q.popleft()

        if n == 100:
            return cnt

        for i in range(1,7):
            next = i+n
            if next > 100: continue
            if visited[next]: continue
            if jump.get(next):
                next = jump[next]
            if not visited[next]:
                visited[next] = 1
                q.append((next,cnt+1))

print(solve())
        
