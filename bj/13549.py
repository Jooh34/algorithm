from collections import deque

N,K = map(int,input().split())
LEN = max(10, max(N,K)*2)

def solution():
    dp = [float('inf')]*LEN
    q = deque([(N, N, 0)])
    visited = [-1] * N
    while q:
        prev, node, move = q.popleft()
        if visited[node] != -1:
            continue
        visited[node] = prev

        if node == K:
            print(move)
            break

        for next in [node-1, node+1, node*2]:
            if 0 <= next < LEN and visited[node] == -1:
                q.append((node, next,move+1))
    
    path = []
    i = K
    while True:
        path.append(i)
        if i == N:
            path.append(visited[i])
            break

        i = visited[i]

    
    print(path[::-1])
  
solution()