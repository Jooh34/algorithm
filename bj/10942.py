import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))

palin = [[False]*N for _ in range(N)]

for i in range(N):
    palin[i][i] = True

for i in range(N-1):
    palin[i][i+1] = s[i] == s[i+1]

for j in range(2,N):
    for i in range(N-j): # i+j < N
        palin[i][i+j] = palin[i+1][i+j-1] and (s[i] == s[i+j])

Q = int(input())
for _ in range(Q):
    u,v = map(int, input().split())
    if palin[u-1][v-1]:
        print(1)
    else:
        print(0)