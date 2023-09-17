def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    for i in range(n-1, -1, -1):
        d -= deliveries[i]
        p -= pickups[i]

        loop = 0
        while d < 0 or p < 0:
            d += cap
            p += cap
            loop+=1
        
        answer += (i+1)*2*loop
    
    return answer

q1 = [4,	5,	[1, 0, 3, 1, 2], [0, 3, 0, 4, 0]]
q2 = [2,7,	[1, 0, 2, 0, 1, 0, 2],	[0, 2, 0, 1, 0, 2, 0]]
q3 = [2,2,[0,0],[0,0]]
print(solution(*q1))
print(solution(*q2))
print(solution(*q3))