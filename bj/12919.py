S = input()
T = input()

global answer
answer = 0
def solve():
    def backtrack(t):
        global answer
        if t == S:
            answer = 1
            return

        if len(S) == len(t):
            return
        
        if t[-1] == 'A':
            backtrack(t[:-1])
        if t[0] == 'B':
            backtrack((t[1:])[::-1])

    backtrack(T)

solve()
print(answer)
