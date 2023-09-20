N = int(input())
lst = map(int, input().split())

so = sorted(lst)
k = N
answer = 0
for s in so:
    answer += k*s
    k-=1

print(answer)
