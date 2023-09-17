import queue

MAX=151
def solution(alp, cop, problems):
    dp = [[9999] * MAX for _ in range(MAX)]
    
    target_alp = 0 
    target_cop = 0
    for pr in problems:
        a,c,_,_,_ = pr
        if a > target_alp: target_alp = a
        if c > target_cop: target_cop = c

    problems = [[0,0,1,0,1],[0,0,0,1,1]] + problems

    q = queue.PriorityQueue()
    q.put((0,alp,cop)) # (cost, alp, cop)
    while q:
        cost, alp, cop = q.get()
        
        if alp >= target_alp and cop >= target_cop:
            return cost

        for pr in problems:
            a,c,rwda,rwdc,co = pr
            if a <= alp and c <= cop:
                new_cost = cost+co
                new_alp = min(target_alp,alp+rwda)
                new_cop = min(target_cop,cop+rwdc)
                if dp[new_alp][new_cop] > new_cost:
                    q.put((new_cost, new_alp, new_cop))
                    dp[new_alp][new_cop] = new_cost
    
    return dp[target_alp][target_cop]

q1 = [0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]]
q2 = [10	,10	,[[10,15,2,1,2],[20,20,3,3,4]]]

print(solution(*q1))
print(solution(*q2))