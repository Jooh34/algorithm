from collections import deque

N,K = map(int,input().split())
LEN = max(10, max(N,K)*2)

def solution():
    dp = [float('inf')]*LEN
    q = deque([(N, 0)])
    cnt = 0
    min_move = -1
    while q:
        node, move = q.popleft()
        if dp[node] < move:
            continue
        dp[node] = move

        if node == K:
            min_move = move
            cnt+=1
            break

        for next in [node-1, node+1, node*2]:
            if 0 <= next < LEN and dp[next] >= move+1:
                q.append((next,move+1))

    while q:
        node, move = q.popleft()
        if node == K and move == min_move:
            cnt+=1

    print(min_move)
    print(cnt)

solution()