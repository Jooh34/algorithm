n = int(input())
lst = list(map(int, input().split()))
x = int(input())

lst.sort()
answer=0
l = 0
r = len(lst)-1
while l<r:
    sm = lst[l]+lst[r]
    if sm > x:
        r-=1
    elif sm < x:
        l+=1
    else:
        ori_l=l
        while l<r and lst[l] == lst[ori_l]:
            if lst[l] == lst[ori_l]:
                answer += 1
                l+=1
            else:
                break
        l=ori_l+1

print(answer)