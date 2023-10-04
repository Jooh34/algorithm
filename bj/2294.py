from collections import deque

n,k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

def solution():
    visited = [False]*(k+1)
    q = deque()
    q.append((0,0)) # (num, sum_)
    while q:
        num, sum_ = q.popleft()
        if visited[sum_]:
            continue
        visited[sum_]=True

        for m in money:
            next_sum_ = sum_+m
            if next_sum_ == k:
                return num+1
            if next_sum_ <= k and not visited[next_sum_]:
                q.append((num+1, next_sum_))

    return -1

print(solution())