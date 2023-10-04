n = int(input())
lst = list(map(int, input().split()))
answer = [-1]*n

stack = []
for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] > lst[i]:
            break
        else:
            stack.pop()

    if stack:
        answer[i] = stack[-1]

    stack.append(lst[i])

print(*answer)
