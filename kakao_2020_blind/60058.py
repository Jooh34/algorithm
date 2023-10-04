def check_correct(p):
    '''
    assume that input is balanced
    '''
    stck = []
    for i in range(len(p)):
        if p[i] == '(':
            stck.append(p[i])
        else:
            if stck:
                stck.pop()
            else:
                return False
    
    return True

def make_correct(u, v):
    result = '('
    result += recur(v)
    result += ')'
    
    flip_u = ''
    u = u[1:-1]
    for i in range(len(u)):
        if u[i] == '(':
            flip_u += ')'
        else:
            flip_u += '('
    
    result += flip_u
    return result

def recur(p):
    #1
    if p == '':
        return ''
    
    #2
    l = 0
    r = 0
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        else:
            r += 1
        
        if l == r:
            break
    
    u = p[:i+1]
    v = p[i+1:]

    # print(u,v)
    if check_correct(u):
        return u + recur(v)

    else:
        return make_correct(u,v)

def solution(p):
    return recur(p)

ql = ["(()())()", ")(", "()))((()"]
for q in ql:
    print(solution(q))