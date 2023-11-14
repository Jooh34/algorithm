N = int(input())
INF = 1e9

global answer
answer = INF

score = []
for _ in range(N):
    row = list(map(int, input().split()))
    score.append(row)

def check_min(al,bl):
    a_sum = 0
    b_sum = 0
    for a1 in al:
        for a2 in al:
            if a1 != a2:
                a_sum += score[a1][a2]
    for b1 in bl:
        for b2 in bl:
            if b1 != b2:
                b_sum += score[b1][b2]

    global answer
    answer = min(answer,abs(a_sum-b_sum))

def teamming(a,b,i):
    if i == N:
        check_min(a,b)
        return

    if len(a) < N//2:
        teamming(a+[i],b,i+1)
    if len(b) < N//2 and i != 0:
        teamming(a,b+[i],i+1)

teamming([],[],0)
print(answer)