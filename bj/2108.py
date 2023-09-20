import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
lst = []
sum_ = 0
d = defaultdict(int)
for _ in range(N):
    n = int(input())
    sum_ += n
    d[n] += 1
    lst.append(n)

lst.sort()

average = round(sum_/len(lst)) 
median = lst[len(lst)//2]
range_ = lst[len(lst)-1]-lst[0]

max_value = 0
candidate = []
for k,v in d.items():
    if v > max_value:
        max_value = v
        candidate = [k]
    elif v == max_value:
        candidate.append(k)

if len(candidate) == 1:
    mode = candidate[0]
else:
    candidate.sort()
    mode = candidate[1]

print(average)
print(median)
print(mode)
print(range_)