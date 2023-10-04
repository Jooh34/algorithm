import sys
input = sys.stdin.readline 

N = int(input())
lst = list(map(int, input().split(' ')))
S = int(input())

sorted_index = 0
while S > 0 and sorted_index < len(lst):
    max_i = sorted_index
    max_v = 0
    for i in range(sorted_index, min(sorted_index+S+1,N)):
        if lst[i] > max_v:
            max_v = lst[i]
            max_i = i
    
    # bubble max value
    for i in range(max_i, sorted_index, -1):
        temp = lst[i]
        lst[i] = lst[i-1]
        lst[i-1] = temp
        S -= 1
        if S == 0:
            break
    
    sorted_index += 1

print(' '.join(list(map(str,lst))))