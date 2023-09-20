def n_combo(lst, n):
    if n == 0:
        return [[]]
    
    result = []
    for i in range(len(lst)):
        m = lst[i]
        rem = lst[i:]

        rem_list = n_combo(rem, n-1)
        for r in rem_list:
            result.append([m, *r])

    return result

    
N,M = map(int,input().split())
lst = [i+1 for i in range(N)]
for l in n_combo(lst,M):
    print(*l)