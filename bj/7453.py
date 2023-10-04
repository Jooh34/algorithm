import sys
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(4)]
answer = 0
for _ in range(N):
    els = list(map(int, input().split()))
    for i,el in enumerate(els):
        lst[i].append(el)

left = []
right = []
for i in range(N):
    for j in range(N):
        left.append(lst[0][i] + lst[1][j])
        right.append(lst[2][i] + lst[3][j])

left.sort()
right.sort()

l = 0
r = len(right)-1
while r >= 0 and l < len(left):
    sm = left[l] + right[r]
    if sm == 0:
        left_same = 0
        original_l = l
        while l < len(left):
            if left[l] == left[original_l]:
                left_same+=1
                l+=1
            else:
                break


        right_same = 0
        original_r = r
        while r >= 0:
            if right[r] == right[original_r]:
                right_same+=1
                r-=1
            else:
                break

        answer += (left_same*right_same)
    
    elif sm < 0:
        l += 1
    
    else:
        r -= 1

print(answer)