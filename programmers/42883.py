def solution(number, k):
    answer=''
    remain = len(number) - k

    i = 0
    while remain > 0 :
        end = len(number)-remain+1

        max = -1
        max_index = -1
        while i < end:
            if int(number[i]) > max:
                max = int(number[i])
                max_index = i
                if max == 9:
                    break
        
            i+=1
        
        answer += number[max_index]
        remain-=1
        i = max_index+1

    return answer

print(solution("1924",2))
print(solution("1924",3))
print(solution("1231234",3))
print(solution("1231234",6))
print(solution("4177252841",4))
print(solution("9999999999",1))
print(solution("123987",3))
