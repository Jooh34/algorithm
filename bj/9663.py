n = int(input())
lst = [0]*n
answer = 0

def check(col, row) :
    for c in range(col) :
        if lst[c] == row : return False
        if (col-c) == abs(row-lst[c]) : return False
    return True

def dfs(col) :
    global answer
    if col == n:
        answer += 1
        return

    for row in range(n) :
        lst[col] = row
        if check(col, row):
            dfs(col+1)

dfs(0)
print(answer)