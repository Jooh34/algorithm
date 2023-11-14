N = int(input())
lst = list(map(int,input().split()))
dp = [0]*N
re_dp = [0]*N

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
record = [0]*N
for i in range(N):
    if len(LIS) == 0 or LIS[-1] < lst[i]:
        LIS.append(lst[i])
    else:
        idx = lower_bound(LIS, lst[i])
        LIS[idx] = lst[i]

    record[i] = len(LIS)

# reverse
LIS = []
rev_record = [0]*N
for i in range(N-1,-1,-1):
    if len(LIS) == 0 or LIS[-1] < lst[i]:
        LIS.append(lst[i])
    else:
        idx = lower_bound(LIS, lst[i])
        LIS[idx] = lst[i]

    rev_record[i] = len(LIS)

mx = 0
for i in range(N):
    mx = max(mx,record[i]+rev_record[i]-1)

print(mx)