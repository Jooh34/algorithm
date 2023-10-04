N = int(input())
lst = list(map(int, input().split()))
m = max(lst)
lst = [i/m*100 for i in lst]
print(sum(lst)/N)