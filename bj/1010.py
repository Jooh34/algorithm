import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    a,b = map(int,input().split())
    n = a if a>b else b
    r = b if a>b else a

    nfac = 1
    n_rfac = 1
    rfac = 1
    for i in range(1,n+1):
        nfac *= i

    for i in range(1, n-r+1):
        n_rfac *= i

    for i in range(1,r+1):
        rfac *= i
    
    answer = nfac // (n_rfac*rfac)
    print(answer)    
