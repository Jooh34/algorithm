import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N,K = map(int, input().split())
jews = []
bags = []
for _ in range(N):
    M,V = map(int, input().split())
    jews.append((M,V))

for _ in range(K):
    bag = int(input())
    bags.append(bag)

jews.sort(key=lambda x:x[0])
bags.sort()

answer = 0
i = 0
q = []
for b in bags:
    while i < len(jews) and b >= jews[i][0]:
        heappush(q, -jews[i][1])
        i+=1
    if q:
        answer -= heappop(q)

print(answer)