import math

n = int(input())
lst = list(map(int, input().split()))

EPS = 1e-9
answer = [0]*n
for i in range(n):
    for j in range(i+1,n):
        see = True

        diff = lst[j]-lst[i]
        level = diff / (j-i)
        mult = 1
        for k in range(i+1, j):
            if lst[k] < math.ceil(lst[i]+level*mult):
                pass
            else:
                see=False
            
            mult+=1

        if see:
            answer[i]+=1; answer[j]+=1
        
print(max(answer))
