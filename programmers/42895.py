from itertools import product

def solution(N, number):
    s_list = [set() for _ in range(9)]

    for i in range(1,9):
        for j in range(1,i):
            prod = product(list(s_list[i-j]), list(s_list[j]))
            for a,b in prod:
                s_list[i].add(a+b)
                s_list[i].add(a-b)
                s_list[i].add(a*b)
                if b != 0: s_list[i].add(a//b)

        s_list[i].add(int(str(N)*i))
        if number in s_list[i]:
            return i
    
    return -1


# 2 => (1,1)
# 3 => (2,1)
# 4 => (3,1), (2,2)
# 5 => (4,1), (3,2)
q1 = [5,12]
q2 = [2,11]
q3 = [5,31168]
q4 = [5,5]
print(solution(*q1))
print(solution(*q2))
print(solution(*q3))
print(solution(*q4))