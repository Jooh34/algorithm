import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
q = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if q:
            print(heappop(q))
        else:
            print(0)
    else:
        heappush(q, n)
