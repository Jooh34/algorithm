import sys
input = sys.stdin.readline
K = int(input())
stck = []
for _ in range(K):
    n = int(input())
    if n == 0:
        stck.pop()
    else:
        stck.append(n)

print(sum(stck))