n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

answer = 0

stack = []
for i in range(n-1,-1,-1):
    popped = None
    while stack:
        if stack[-1][0] > lst[i]:
            answer += 1
            break
        else:
            answer += stack[-1][1]
            popped = stack.pop()

    if popped != None and popped[0] == lst[i]:
        new = (popped[0], popped[1]+1)
        stack.append(new)
    else:
        stack.append((lst[i],1))


print(answer)
