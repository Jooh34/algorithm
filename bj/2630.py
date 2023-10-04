import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    lst = list(map(int, input().split()))
    m.append(lst)

global white, blue
white = 0
blue = 0
def solve(x,y,size):
    global white, blue
    if size == 1:
        if m[x][y] == 1:
            blue+=1
        else:
            white+=1
        return

    num = m[x][y]
    for r in range(x,x+size):
        for c in range(y,y+size):
            if m[r][c] != num:
                x_mid = x+size//2
                y_mid = y+size//2
                solve(x,y,size//2)
                solve(x_mid,y,size//2)
                solve(x,y_mid,size//2)
                solve(x_mid,y_mid,size//2)
                return

    
    if num == 1:
        blue+=1
    else:
        white+=1

solve(0,0,n)
print(white)
print(blue)