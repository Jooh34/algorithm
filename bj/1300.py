N = int(input())
k = int(input())
MAX = 10000000000

def check(x):
    cnt = 0
    for i in range(1,N+1):
        cnt += min(x//i,N)
    return cnt
    

def bisect_lower(mx):
    l = 0
    r = mx+1

    while l<r:
        mid = (l+r)//2
        x = check(mid)
        if x < k:
            l = mid+1
        else:
            r = mid

    return l

print(bisect_lower(MAX))