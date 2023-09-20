from itertools import combinations
N,M = map(int,input().split())
lst = [i+1 for i in range(N)]
for l in list(combinations(lst,M)):
    print(*l)