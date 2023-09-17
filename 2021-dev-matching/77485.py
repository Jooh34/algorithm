def solution(rows, columns, queries):
    answer = []
    b = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(r*columns+c+1)
        b.append(row)

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    for q in queries:
        lst = []
        x1,y1,x2,y2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1
        xx = x1
        yy = y1
        lst.append(b[xx][yy])
        for dx,dy in dirs:
            while True:
                xx+=dx
                yy+=dy
                if xx > x2:
                    xx -= 1
                    break
                elif xx < x1:
                    xx += 1
                    break
                elif yy > y2:
                    yy -= 1
                    break
                elif yy < y1:
                    yy += 1
                    break
                
                lst.append(b[xx][yy])

        answer.append(min(lst))

        del lst[len(lst)-1]
        xx = x1
        yy = y1+1
        i=0
        b[xx][yy] = lst[i]
        for dx,dy in dirs:
            while True:
                i+=1
                xx+=dx
                yy+=dy
                if xx > x2:
                    xx -= 1
                    i-=1
                    break
                elif xx < x1:
                    xx += 1
                    i-=1
                    break
                elif yy > y2:
                    yy -= 1
                    i-=1
                    break
                elif yy < y1:
                    yy += 1
                    i-=1
                    break
                
                if i < len(lst):
                    b[xx][yy] = lst[i]
        # print(b)

    return answer


q1 = [3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]]
q2 = [6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]]
print(solution(*q2))