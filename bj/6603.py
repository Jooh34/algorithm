from itertools import combinations
import sys
input = sys.stdin.readline

def n_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        rem = lst[i+1:]
        rem_combo = n_combo(rem, n-1) 
        for c in rem_combo:
            l.append([m,*c])

    return l

while True:
    lst = list(map(int,input().split(' ')))
    if lst[0] == 0:
        break
    combo = n_combo(lst[1:],6)
    for c in combo:
        print(' '.join(map(str,c)))
    print('')