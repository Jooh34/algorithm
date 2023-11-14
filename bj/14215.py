def solve():
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[2] >= lst[0]+lst[1]:
        return 2*(lst[0]+lst[1])-1
    else:
        return sum(lst)
    
print(solve())