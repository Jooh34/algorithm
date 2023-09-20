def solution(n):
    answer = list(subproblem(n, 1, 3, 2))
    return answer

def subproblem(n, from_, to_, stopover_):
    if n == 1:
        yield [from_, to_]
    else:
        yield from subproblem(n-1, from_, stopover_, to_)
        yield [from_, to_]
        yield from subproblem(n-1, stopover_, to_, from_)

N = int(input())

sol = solution(N)
print(len(sol))
for s in sol:
    print(*s)