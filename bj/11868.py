n = int(input())
lst = list(map(int, input().split()))

grundy = 0
for el in lst:
    grundy ^= el

if grundy:
    print('koosaga')
else:
    print('cubelover')