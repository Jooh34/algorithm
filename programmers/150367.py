import math

def check(number: str):
    # n : 3, 7, 15, 24 ... (n^2-1)
    n = len(number)

    root = ((n+1)//2) - 1
    h = int(math.log(n+1, 2)) - 1

    if number[root] == '0': return 0

    q = [(root, h, '1')] # (index, height, parent_number)
    while q:
        i, h, parent = q.pop(-1)
        if parent == '0' and number[i] == '1': # impossible
            return 0

        if h == 0: # leaf node
            continue        
        
        move = int(math.pow(2, h-1))
        #right
        q.append((i+move, h-1, number[i]))

        #left
        q.append((i-move, h-1, number[i]))

    return 1 

def solution(numbers):
    answer = []
    for n in numbers:
        bi = ''
        while n > 0:
            bi = str(n % 2) + bi
            n = n // 2

        idx = 1
        while len(bi) > (2**idx)-1:
            idx += 1

        bi = '0' * ((2**idx)-1-len(bi)) + bi
        answer.append(check(bi))

    return answer

q1 = [7, 42, 5]
q2 = [63, 111, 95]
q3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 1099511627775]
# print(solution(q1))
# print(solution(q2))
print(solution(q3))