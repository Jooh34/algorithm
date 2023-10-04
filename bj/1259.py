import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    
    mid = len(s) // 2
    if len(s) % 2 == 0:
        a = s[:mid]
        b = s[mid:]
    else:
        a = s[:mid]
        b = s[mid+1:]

    if a == b[::-1]:
        print("yes")
    else:
        print("no")
