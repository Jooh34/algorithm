import math

def solve():
    px = [0]*3; py = [0]*3
    px[0], py[0] = map(int, input().split())
    px[1], py[1]= map(int, input().split())
    px[2], py[2] = map(int, input().split())

    def dot(v1,v2):
        return v1[0]*v2[0]+v1[1]*v2[1]
    def det(v1,v2):
        return v1[0]*v2[1] - v1[1]*v2[0]

    v1 = (px[0]-px[1], py[0]-py[1])
    v2 = (px[2]-px[1], py[2]-py[1])
    angle = math.atan2(det(v1,v2), dot(v1,v2))

    if angle == math.pi or angle == 0:
        return 0
    elif angle < 0:
        return 1
    else:
        return -1

print(solve())