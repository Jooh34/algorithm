import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
lst = list(map(int, input().split()))
klist = list(map(int, input().split()))
    
lst.sort()
parent = [i for i in range(N+1)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])

    return parent[u]

def union_(u, v):
    pu = find(u)
    pv = find(v)
    if pu < pv:
        parent[u] = pv
    else:
        parent[v] = pu

def lower_bound(inlst, x):
    left = 0
    right = len(inlst)
    while left<right:
        mid = (left+right)//2
        if x >= inlst[mid]:
            left = mid+1
        else:
            right = mid
    
    return left
    
for k in klist:
    idx = find(lower_bound(lst,k))
    print(lst[idx])
    union_(idx,idx+1)