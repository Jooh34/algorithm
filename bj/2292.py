N = int(input())

# 1 7 19 37 61
# 6 12 18 24 ..
i = 1
k = 6
answer = 1
while i < N:
    answer += 1
    i += k
    k += 6

print(answer)