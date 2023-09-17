from heapq import heappush, heappop
def solution(prices):
    answer = [0] * len(prices)
    q = []
    for i,p in enumerate(prices):
        while q:
            v, index = heappop(q)
            if -v > p: # drop
                answer[index] = i-index
            else: # no drop on q
                heappush(q, (v,index))
                break
            
        heappush(q, (-p,i))
    
    while q:
        v,index = heappop(q)
        answer[index] = i-index

    return answer

print(solution([2,1]))