import sys
input = sys.stdin.readline

N,S = map(int,input().split())
lst = list(map(int, input().split()))

prefix_sum = [0] * (N+1)
for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

l=0
r=1
MAX = 100000000
answer = MAX
while r < N+1:
    if r == l:
        r+=1
        continue

    sum_ = prefix_sum[r]-prefix_sum[l]
    # print(sum_, S)
    if sum_ >= S:
        answer = min(answer, (r-l))
        l+=1
    else:
        r+=1

if answer == MAX:
    print(0)
else:
    print(answer)