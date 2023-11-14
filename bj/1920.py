n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))

lst.sort()

def bsearch(x, in_lst):
    l = 0
    r = len(in_lst)
    while l<r:
        mid = (l+r)//2
        if in_lst[mid] < x:
            l = mid+1
        elif in_lst[mid] > x:
            r = mid
        else:
            return 1

    return 0

for i in lst_m:
    x = bsearch(i,lst)
    print(x)