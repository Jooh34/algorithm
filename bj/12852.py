from collections import deque

INF = 1e9
N = int(input())
dp = [INF]*(N+1)
dp_parent = [-1]*(N+1)

dp[N]=0
q = deque([])
q.append((N,-1,0)) # i, prarent, cnt
while q:
    i,parent, cnt = q.popleft()
    if dp[i] < cnt:
        continue
    dp[i] = cnt
    dp_parent[i] = parent

    if i == 1:
        print(cnt)
        break
    
        
    if i % 3 == 0 and dp[i//3] > cnt+1:
        q.append((i//3,i,cnt+1))
    if i % 2 == 0 and dp[i//2] > cnt+1:
        q.append((i//2,i,cnt+1))
    if dp[i-1] > cnt+1:
        q.append((i-1,i,cnt+1))

lst = []
n = 1
while n != -1:
    lst.append(n)
    n = dp_parent[n]
lst.reverse()
print(*lst)