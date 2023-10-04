from collections import deque

n = int(input())
lst = deque([(i,int(num)) for i,num in enumerate(input().split())])

answer = [1]
k = lst.popleft()
while lst:
    i = k[1]
    if i > 0:
        while True:
            i-=1
            v = lst.popleft()
            if i == 0:
                k = v
                answer.append(v[0]+1)
                break
            else:
                lst.append(v)

    elif i < 0:
        while True:
            i+=1
            v = lst.pop()
            if i == 0:
                k = v
                answer.append(v[0]+1)
                break
            else:
                lst.appendleft(v)

print(*answer)