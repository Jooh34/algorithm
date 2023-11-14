K, N = map(int, input().split())
lst = []
mx = 1_000_000_000
lst = list(map(int, input().split()))

def check(x):
    _sum = 0
    for el in lst:
        _sum += max(0,el-x)
    
    if _sum >= N:
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

print(bisect(mx))