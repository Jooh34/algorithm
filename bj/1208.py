import sys
input = sys.stdin.readline
from collections import defaultdict

N,S = map(int,input().split())
lst = list(map(int,input().split()))
subsum = defaultdict(int)
global answer
answer = 0

def right_seq(start, sum_):
    if start == N:
        subsum[sum_]+=1
        return
    right_seq(start+1, sum_+lst[start]) # use list[start]
    right_seq(start+1, sum_) # not use

def left_seq(start, sum_):
    global answer
    if start == N//2:
        answer += subsum[S-sum_]
        return
    
    left_seq(start+1, sum_+lst[start])
    left_seq(start+1, sum_)

right_seq(N//2, 0)
left_seq(0,0)
if S == 0: # left and right all 0 case
    answer -= 1

print(answer)

    
        



