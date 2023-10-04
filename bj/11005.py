N,B = map(int, input().split())

s = ''
while N:
    rem = N%B
    if 0 <= rem <= 9:
        s = str(rem) + s
    else:
        s = chr(ord('A') + (rem - 10)) + s

    N = N // B

print(s)