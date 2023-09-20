def find(a,sortB):
    left=0
    right=len(sortB)
    while left<right:
        mid = (left+right)//2
        if a < sortB[mid]:
            right = mid
        else:
            left = mid+1
    
    return left

def solution(A, B):
    answer = 0
    sortB = sorted(B)
    for a in A:
        index = find(a,sortB)
        if index == len(sortB): # no candidate
            continue
        else:
            answer += 1
            del sortB[index]
    return answer


q1 = [[5,2,2,7,9],[2,2,6,8,10]]
q2 = [[2,2,2,2],[1,1,1,1]]
print(solution(*q1))
print(solution(*q2))