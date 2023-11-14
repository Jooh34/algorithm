def solve():
    n = int(input())
    lst = [0]
    lst_in = list(map(int, input().split()))
    lst = lst+lst_in

    visited = [0] * (n+1)

    def check(x):
        group = []

        nx = x
        while visited[nx] == 0:
            visited[nx] = 1
            group.append(nx)
            nx = lst[nx]
        
        for i,g in enumerate(group):
            if g == nx:
                return len(group) - i
        
        else:
            return 0

    answer = 0    
    for i in range(1,n+1):
        if visited[i]:
            continue

        cnt = check(i)
        answer += cnt

    return n-answer

T = int(input())
for _ in range(T):
    print(solve())