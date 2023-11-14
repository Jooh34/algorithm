import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heappush(q,(abs(x), x))
    else:
        if q:
            _, v = heappop(q)
            print(v)
        else:
            print(0)
