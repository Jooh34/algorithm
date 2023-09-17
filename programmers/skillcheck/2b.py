def solution(m, n, startX, startY, balls):
    answer = []
    for ballX,ballY in balls:
        lst = []
        if startY != ballY or ballX > startX:
            left = (startX+ballX)**2 + (startY-ballY)**2
            lst.append(left)
        
        if startY != ballY or ballX < startX:
            right = ((m-startX)+(m-ballX))**2 + (startY-ballY)**2
            lst.append(right)

        if startX != ballX or ballY > startY:
            down = (startY+ballY)**2 + (startX-ballX)**2
            lst.append(down)

        if startX != ballX or ballY < startY:
            up = ((n-startY)+(n-ballY))**2 + (startX-ballX)**2
            lst.append(up)
            
        answer.append(sorted(lst)[0])

    return answer

q1 = [10,	10,	3,	7,	[[7, 7], [2, 7], [7, 3]]]
print(solution(*q1))