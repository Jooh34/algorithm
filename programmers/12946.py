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

# def subproblem(n, from_, to_, stopover_):
#     if n == 1:
#         return [[from_, to_]]
#     else:
#         ans = []
#         ans.extend(subproblem(n-1, from_, stopover_, to_))
#         ans.extend([[from_, to_]])
#         ans.extend(subproblem(n-1, stopover_, to_, from_))
#         return ans


print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))