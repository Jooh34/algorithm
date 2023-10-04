def solution():
    N = input()

    digit = len(N)-1
    n = max(10**(digit-1),1)
    intN = int(N)

    while n < intN:
        result = n + sum(map(int,list(str(n))))
        if result == intN:
            return n

        n+=1

    return 0

print(solution())