def solution(N, B):
    answer = 0
    for i in range(len(N)-1,-1,-1):
        ch = N[i]
        if ord('0') <= ord(ch) <= ord('9'):
            num = ord(ch)-ord('0')
        else:
            num = ord(ch)-ord('A')+10

        answer += B**(len(N)-i-1) * num
    return answer

N,B = input().split(' ')
print(solution(N,int(B)))