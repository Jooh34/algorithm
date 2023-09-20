N = int(input())
answer = 0
plus = []
minus = []
zeros = 0
for _ in range(N):
    n = int(input())
    if n > 0:
        plus.append(n)
    elif n < 0:
        minus.append(n)
    else:
        zeros+=1

plus = sorted(plus,reverse=True)
minus = sorted(minus)
# for plus
q = []
for p in plus:
    if p == 1:
        answer+=p
    elif q:
        answer += p*q.pop()
    else:
        q.append(p)
if q:
    answer += q.pop()

# for minus
q = []
for m in minus:
    if q:
        answer += m*q.pop()
    else:
        q.append(m)

if q and zeros == 0:
    answer += q.pop()

print(answer)