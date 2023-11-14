#LIS

def lower_bound(lst,x):
    l = 0 
    r = len(lst)
    while l<r:
        mid = (l+r)//2
        if lst[mid] < x:
            l = mid+1
        else:
            r = mid

    return l
    
N = int(input())
in_lst = list(map(int, input().split()))

lis = []
record = [0]*N

for i,el in enumerate(in_lst):
    if not lis or lis[-1] < el:
        lis.append(el)
        record[i] = len(lis)

    else:
        idx = lower_bound(lis,el)
        lis[idx] = el
        record[i] = idx+1
    
print(len(lis))
n = len(lis)
answer = []
for i in range(len(in_lst)-1,-1,-1):
    if record[i] == n:
        answer.append(in_lst[i])
        n -= 1

answer.reverse()
print(*answer)