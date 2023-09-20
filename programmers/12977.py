from itertools import combinations

def is_prime(n):
    if n == 0 or n == 1:
        return False

    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        
        i+=1

    return True
    
def solution(nums):
    answer = 0
    
    lst = list(combinations(nums, 3))
    for l in lst:
        if is_prime(sum(l)):
            answer += 1

    return answer

q = [[1,2,3,4], [1,2,7,6,4]]
for a in q:
    print(solution(a))