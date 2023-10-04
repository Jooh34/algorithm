import sys
input = sys.stdin.readline
N = int(input())
geometry = "geometry"
number_theory = "number_theory"
hanbyeol = "hanbyeol"

for _ in range(N):
    s,n,u,p,c = map(int, input().split())
    if s == 0 and n == 0 and u == 0:
        if p % 2 == 0:
            print(number_theory)
        else:
            print(geometry)

    elif s == 0 and n == 0:
        if u == 1:
            if p % 2 == 1:
                print(geometry)
            else:
                print(hanbyeol)

        else:
            print(hanbyeol)

    else:
        print(hanbyeol)
