n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))

lst.sort()

def lower_bound(x, in_lst):
    l = 0
    r = len(in_lst)
    while l<r:
        mid = (l+r)//2
        if in_lst[mid] < x:
            l = mid+1
        else:
            r = mid

    return l

def upper_bound(x, in_lst):
    l = 0
    r = len(in_lst)
    while l<r:
        mid = (l+r)//2
        if in_lst[mid] <= x:
            l = mid+1
        else:
            r = mid

    return l

for i in lst_m:
    u = upper_bound(i,lst)
    l = lower_bound(i,lst)
    print(u-l, end=' ')