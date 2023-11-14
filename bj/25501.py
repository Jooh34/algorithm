T = int(input())

def is_palin(s, n):
    if len(s) == 1 or len(s) == 0:
        return (1, n)

    if s[0] == s[len(s)-1]:
        return is_palin(s[1:len(s)-1], n+1)
    else:
        return (0, n)

for _ in range(T):
    s = input()
    print(*is_palin(s,1))