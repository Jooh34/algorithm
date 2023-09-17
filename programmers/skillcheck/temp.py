def solution(x, n):
    if x == 0:
        return [0]*n
    return [i for i in range(x,x*(n+1),x)]

print(solution(0,1000))