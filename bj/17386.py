x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

v1 = (x1,y1)
v2 = (x2,y2)
v3 = (x3,y3)
v4 = (x4,y4)
def ccw(v1,v2,v3):
    s = v1[0]*v2[1] + v2[0]*v3[1] + v3[0]*v1[1]
    s -= (v2[0]*v1[1] + v3[0]*v2[1] + v1[0]*v3[1])
    if s > 0: return 1
    elif s == 0: return 0
    else: return -1

p1p2 = ccw(v1,v2,v3) * ccw(v1,v2,v4)
p3p4 = ccw(v3,v4,v1) * ccw(v3,v4,v2)

if p1p2 == -1 and p3p4 == -1:
    print(1)
else:
    print(0)
