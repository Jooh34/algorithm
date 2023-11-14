import sys
input = sys.stdin.readline
write = sys.stdout.write

lst = []
E = int(input())
for _ in range(E):
    u,v = map(int, input().split())
    lst.append((u,v))
    
lst = sorted(lst, key=lambda x : x[1])
a_list = [el[0] for el in lst]

def lower_bound(inlst, n):
    left = 0
    right = len(inlst)
    while left<right:
        mid = (right+left) // 2
        if inlst[mid] < n:
            left = mid+1
        else:
            right = mid

    return left

LIS = []
for i,el in enumerate(a_list):
    el = lst[i]
    if len(LIS) == 0 or LIS[len(LIS)-1] < el:
        LIS.append(el)
        continue
    
    lowerbound = lower_bound(LIS, el)
    LIS[lowerbound] = el

print(E-len(LIS))