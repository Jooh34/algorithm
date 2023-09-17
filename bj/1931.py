import sys, functools
input = sys.stdin.readline

N = int(input())
time = []
for n in range(N):
    a,b = map(int, input().split())
    time.append((a,b))

def cmp(a,b):
    if a[1] != b[1]:
        return a[1]-b[1]
    else:
        return a[0]-b[0]

answer = 0
last = -1
for t in sorted(time, key=functools.cmp_to_key(cmp)):
    if last <= t[0]:
        last = t[1]
        answer+=1

print(answer)