def check_sittable(b):
    pass

def check_adj(b):
    pass

def check_front(front, b):
    pass

def solve():
    N,M = map(int, input().split())
    seat = []
    for _ in range(N):
        row = input().split()
        seat.append(row)

    # dp[row][state], state -> bit masking
    dp = [[-1]*M for _ in range(N)]

    bit_set = [] # bits set that isn't adjacent
    for b in range(0, (1 << M)):
        if check_adj(b):
            bit_set.append(b)

    row_bitmask_max = 2**(M+1)-1
    for rb in row_bitmask_max:
        if check_sittable(rb):

    dp[]

T = int(input())
for _ in range(T):
    solve()