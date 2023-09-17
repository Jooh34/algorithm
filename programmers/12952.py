def check(lst, col, row) :
    for c in range(col) :
        if lst[c] == row : return False
        if (col-c) == abs(row-lst[c]) : return False
    return True

def dfs(lst, col, n) :
    result = 0
    for idx in range(n) :
        if check(lst, col, idx) :
            lst[col] = idx
            if col == n-1 : result += 1
            else : result += dfs(lst, col+1, n)

    return result

def solution(n):
    return dfs([0]*n, 0, n)

n = int(input())
print(solution(n))