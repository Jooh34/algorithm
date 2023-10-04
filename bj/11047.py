N,K = map(int,input().split())
answer = 0
money = []
for _ in range(N):
    money.append(int(input()))

for i in range(len(money)-1,-1,-1):
    if K >= money[i]:
        answer += K // money[i]
        K = K % money[i]

print(answer)