n = int(input())
inputlst = list(map(int,list(input())))
target = list(map(int,list(input())))

def solve(first_on, lst, n):
    cnt = 0
    if first_on:
        lst[0]=lst[0]^1
        lst[1]=lst[1]^1
        cnt+=1
    
    for i in range(1,n):
        if lst[i-1] != target[i-1]:
            lst[i-1]=lst[i-1]^1
            lst[i]=lst[i]^1
            if i != n-1:
                lst[i+1]=lst[i+1]^1
            cnt+=1

    
    if lst[n-1] == target[n-1]:
        return cnt
    else:
        return 1e9

a=solve(True, inputlst.copy(), n)
b=solve(False, inputlst, n)
print(min(a,b)) if min(a,b) != 1e9 else print(-1)