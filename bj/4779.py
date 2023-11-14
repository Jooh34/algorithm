def solve(s,l,r):
    d = (r-l)//3
    if d == 0:
        s[l] = '-'
    else:
        solve(s,l,l+d)
        solve(s,r-d,r)

while True:
    try:
        N = int(input())
        l = 3**N
        s = [' ']*l
        solve(s,0,l)
        print(''.join(s))

    except EOFError:
        break