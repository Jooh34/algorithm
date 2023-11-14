n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))

def check(i):
    visited = [0]*(n+1)
    ni = i
    history = []
    while visited[ni] == False:
        history.append(ni)
        visited[ni] = 1
        ni = lst[ni]

    if ni == i:
        return history
    else:
        return []

answer = [0]*(n+1)
for i in range(1,n+1):
    if answer[i] == 0:
        hist = check(i)
        for h in hist:
            answer[h] = 1

print(sum(answer))
for i in range(1,n+1):
    if answer[i]: print(i)
        