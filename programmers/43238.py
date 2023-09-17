
def solution(n, times):
    start = 1
    end = 1000000000*1000000000
    last_succ = 1
    
    while start < end:
        mid = (start+end)//2

        sum = 0
        for time in times:
            sum += mid // time
        
        if n <= sum:
            last_succ = mid
            end = mid
        else:
            start = mid+1
        
    return last_succ


# def check(v, n, times):
#     sum = 0
#     for time in times:
#         sum += v // time
    
#     if n <= sum:
#         return True
#     else:
#         return False

a1 = solution(6, [7,10])
print(a1)