from collections import deque

N,K = map(int,input().split())
LEN = max(10, max(N,K)*2)

def solution():
    v = [False]*LEN
    q = deque([(N, 0)])
    while q:
        node, move = q.popleft()
        if v[node]:
            continue

        if node == K:
            return move

        v[node] = True
        
        for next in [node-1, node+1, node*2]:
            if 0 <= next < LEN and not v[next]:
                q.append((next,move+1))

print(solution())