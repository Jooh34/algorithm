import sys

N = int(sys.stdin.readline().strip())
stck = []
for n in range(N):
    splt = sys.stdin.readline().strip().split(' ')
    c = splt[0]
    if c == 'push':
        stck.append(int(splt[1]))
    elif c == 'pop':
        if stck:
            print(stck.pop())
        else:
            print(-1)
    elif c == 'size':
        print(len(stck))
    elif c == 'empty':
        print(0 if stck else 1)
    elif c == 'top':
        if stck:
            print(stck[len(stck)-1])
        else:
            print(-1)
