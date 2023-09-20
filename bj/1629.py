import sys
input = sys.stdin.readline 
a,b,c = map(int, input().split())

def subproblem(n):
    if n == 1:
        return a
    else:
        n1 = n//2
        if n%2 == 0:
            return subproblem(n1)**2 % c
        else:
            return ((subproblem(n1)**2)*a) % c

print(subproblem(b))