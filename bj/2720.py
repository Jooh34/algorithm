N = int(input())
for _ in range(N):
    n = int(input())
    answer = []
    for coin in [25, 10, 5, 1]:
        answer.append(n // coin)
        n = n % coin

    print(' '.join(map(str,answer)))