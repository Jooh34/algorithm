n = int(input())
lst = list(map(int, input().split()))
INF = 20
answer = [INF]*n

for i in range(n):
    k = lst[i]
    cnt = 0
    for j in range(n):
        if cnt == k and answer[j] == INF:
            answer[j] = i+1
            break
        
        if answer[j] > i+1:
            cnt+=1

print(*answer)
