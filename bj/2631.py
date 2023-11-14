N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

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
for el in lst:
    if not LIS:
        LIS.append(el)
    else:
        if LIS[-1] < el:
            LIS.append(el)
        elif LIS[-1] > el:
            idx = lower_bound(LIS, el)
            LIS[idx] = el

print(N-len(LIS))