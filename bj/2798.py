from itertools import combinations
import sys
input = sys.stdin.readline 

N,M = map(int,input().split())
lst = list(map(int,input().split()))
max_ = 0

for combo in list(combinations(lst, 3)):
    s = sum(combo)
    if M < s:
        continue
    if max_ < s:
        max_ = s

print(max_)
