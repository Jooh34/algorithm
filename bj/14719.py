H,W = map(int,input().split())
lst = list(map(int, input().split()))

left = [0]*W
right = [0]*W
answer = 0

for i in range(1,W):
    left[i] = max(left[i-1],lst[i-1])
for i in range(W-2,-1,-1):
    right[i] = max(right[i+1],lst[i+1])
for i in range(1,W-1):
    mn = min(left[i],right[i])
    answer += max(mn-lst[i],0)

print(answer)