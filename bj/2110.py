MAX = 1_000_000_000

N, C = map(int, input().split())
lst = []
for _ in range(N):
    n = int(input())
    lst.append(n)
lst.sort()

def check(x):
    last = -MAX
    cnt = 0
    for el in lst:
        if el-last >= x:
            cnt += 1
            last = el

    if cnt >= C:
        return 1
    else:
        return 0

def bisect(mx):
    l = 0
    r = mx+1

    answer = 0
    while l<r:
        mid = (l+r)//2
        p = check(mid)
        if p:
            answer = max(answer,mid)
            l = mid+1
        else:
            r = mid

    return answer

print(bisect(MAX))