import sys
input = sys.stdin.readline
from collections import deque

def rb_to_idx(r,b):
    ret = 0
    for i,x in enumerate([*r,*b]):
        ret += x*(10**i)
    return ret

def solve():
    N,M = map(int, input().split())

    R,B,O = None,None,None
    m = []
    visited = [0]*10000
    for i in range(N):
        row = list(input().strip())
        for j in range(M):
            if row[j] == 'R':
                R = (i,j)
                row[j] = '.'
            elif row[j] == 'B':
                B = (i,j)
                row[j] = '.'
            elif row[j] == 'O':
                O = (i,j)

        m.append(row)

    def move(x,y,dx,dy):
        cnt = 0
        nx, ny = x, y
        while m[nx + dx][ny + dy] != '#' and m[nx][ny] != 'O':
            nx += dx
            ny += dy
            cnt += 1
        return nx, ny, cnt

    q = deque([])
    q.append((R,B,0)) # Red, Blue, cnt
    while q:
        r,b,cnt = q.popleft()
        if cnt >= 10:
            return -1
        
        if visited[rb_to_idx(r,b)]:
            continue
        
        visited[rb_to_idx(r,b)] = 1
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            rx,ry,rcnt = move(r[0],r[1],dx,dy)
            bx,by,bcnt = move(b[0],b[1],dx,dy)

            if m[bx][by] == 'O':
                continue

            if m[rx][ry] == 'O':
                return cnt + 1
            
            if rx == bx and ry == by: # overlap
                if rcnt > bcnt:
                    rx,ry = rx-dx,ry-dy
                else:
                    bx, by = bx-dx, by-dy

            new_red = (rx,ry)
            new_blue = (bx,by)
            if not visited[rb_to_idx(new_red,new_blue)]:
                q.append((new_red,new_blue,cnt+1))

    return -1

print(solve())
