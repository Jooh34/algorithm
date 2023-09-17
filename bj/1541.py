st = input()

minus_appear = False
plus = 0
minus = 0
i=0
while i < len(st):
    if st[i] == '+':
        if minus_appear:
            minus += int(st[:i])
        else:
            plus += int(st[:i])
        st = st[i+1:]
        i=0
        continue

    elif st[i] == '-':
        if minus_appear:
            minus += int(st[:i])
        else:
            plus += int(st[:i])
        minus_appear = True
        st = st[i+1:]
        i=0
        continue
    
    i += 1

if minus_appear:
    minus += int(st[:i])
else:
    plus += int(st[:i])

print(plus-minus)
        