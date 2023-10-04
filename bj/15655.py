def n_combo(lst, n):
    if n == 0:
        return [[]]
    
    result = []
    for i in range(len(lst)):
        m = lst[i]
        rem = lst

        rem_list = n_combo(rem, n-1)
        for r in rem_list:
            result.append([m, *r])

    return result

    
N,M = map(int,input().split())
lst = list(map(int, input().split()))
lst.sort()
for l in n_combo(lst,M):
    print(*l)