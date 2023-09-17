def solution(n):
    val = [0] * 100001
    val[1] = 1

    i = 2
    while i <= n:
        val[i] = (val[i-1] + val[i-2]) % 1234567
        i+=1

    return val[n]

print(solution(3))
print(solution(5))
print(solution(100000))