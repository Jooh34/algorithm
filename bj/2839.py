def solution(n):
    five = n // 5
    while five >= 0:
        rem = n-(five*5)
        if rem % 3 == 0:
            three = rem // 3
            return five+three
        
        five -= 1

    return -1

n = int(input())
print(solution(n))