def solution(N):
    if N==1: return '1/1'
    n = 1
    i = 1
    while True:
        n+=i
        if N < n:
            break

        i+=1

    if i%2 == 1:
        numer = n-N
        den = i+1-(numer)
    else:
        den = n-N
        numer = i+1-(den) 
    
    return str(numer) + '/' + str(den)   

N = int(input())
print(solution(N))