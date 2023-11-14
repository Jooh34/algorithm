import sys
sys.setrecursionlimit(10**6)

N = int(input())
div_to = 1000000007

d = {}
d[1] = 1
d[2] = 1
d[3] = 2
def fibo(x):
    if d.get(x) != None:
        return d[x]

    if x % 2 == 0:
        n = x//2
        fibo(n+1)
        fibo(n)
        fibo(n-1)
        v = d[n+1]*d[n] + d[n]*d[n-1]
    else:
        n = (x-1)//2
        fibo(n+1)
        fibo(n)
        v = d[n+1]**2 + d[n]**2

    v = v % div_to
    d[x] = v
    return v

print(fibo(N))