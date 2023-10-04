import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    
    dp00 = [0]*N
    dp01 = [0]*N
    dp01[0] = second[0]
    dp10 = [0]*N
    dp10[0] = first[0]

    for i in range(1,N):
        dp00[i] = max(dp01[i-1], dp10[i-1])
        dp01[i] = max(dp10[i-1], dp00[i-1]) + second[i]
        dp10[i] = max(dp01[i-1], dp00[i-1]) + first[i]
    
    print(max(dp00[N-1], dp01[N-1], dp10[N-1]))