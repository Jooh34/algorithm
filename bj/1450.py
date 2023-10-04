N,C = map(int, input().split())
lst = list(map(int, input().split()))
r_lst = []
global answer
answer = 0

def lower_bound(inlst, x):
    l = 0
    r = len(inlst)
    while l < r:
        mid = (l+r) // 2
        if inlst[mid] <= x:
            l = mid+1
        else:
            r = mid

    return l

def right(st, x):
    if st == N:
        r_lst.append(x)
        return

    right(st+1, x+lst[st])
    right(st+1, x)

def left(st, x):
    global answer
    if st == (N//2):
        target = C-x
        cnt = lower_bound(r_lst, target)
        answer += cnt
        return
    
    left(st+1, x+lst[st])
    left(st+1, x)

right(N//2, 0)
r_lst.sort()
left(0, 0)
print(answer)
