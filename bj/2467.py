n = int(input())
lst = list(map(int,input().split()))

diff_min = 2e9
answer = []

s=0
e=len(lst)-1
while s<e:
    sm = lst[s]+lst[e]
    if abs(sm) < diff_min:
        diff_min = abs(sm)
        answer = [lst[s], lst[e]]
    if sm < 0:
        s += 1
    elif sm > 0:
        e -= 1
    else:
        break

print(*answer)