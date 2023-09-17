import sys
input = sys.stdin.readline

from heapq import heapify, heappop

N,K = map(int,input().split())
nums = list(map(int,input().split()))
heapify(nums)

answer = 0
for _ in range(K):
    answer = heappop(nums)

print(answer)