s = input()
sub = input()
sub = list(reversed(sub))

stck = []
for ch in s:
    stck.append(ch)
    if len(stck) >= len(sub):
        bomb = True
        for i in range(len(sub)):
            if stck[-i-1] != sub[i]:
                bomb = False
                break

        if bomb:
            for _ in range(len(sub)):
                stck.pop()

if stck:
    print(''.join(stck))
else:
    print('FRULA')
