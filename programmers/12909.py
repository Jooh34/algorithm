def solution(s):
    stck = []
    for ch in s:
        if ch == '(':
            stck.append(ch)
        else:
            if stck:
                stck.pop()
            else:
                return False
    
    if not stck:
        return True
    else:
        return False

ql = ["()()"]
for q in ql:
    print(solution(q))