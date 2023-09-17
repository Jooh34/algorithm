import math
from collections import deque

def solution(operations):
    dq = deque([])
    for op in operations:
        print(dq)
        s = op.split(" ")
        val = int(s[1])
        
        if s[0] == "I":
            insert(dq, val)
        else:
            if not dq : continue
        
            if val > 0:
                dq.pop()
            else:
                dq.popleft()

    answer = [0, 0]
    if dq:
        answer = [dq[-1], dq[0]]
    
    return answer

def insert(dq, val):
    start = 0
    end = len(dq)
    
    while start < end:
        mid = math.floor((start+end)/2)
        if dq[mid] < val:
            if start == mid: break
            start = mid
        else:
            end = mid
        
    dq.insert(end, val)


q1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
q2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333", "D 1"]
q3 = ["I 5", "I 1", "I 10", "I 3", "I 4", "I 8", "I 9", "I 2"]
print(solution(q1))
print(solution(q2))
print(solution(q3))