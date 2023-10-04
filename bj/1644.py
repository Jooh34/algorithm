N = int(input())

prime = [1 for _ in range(N+1)]
i=2
while i*i <= N:
    if prime[i]:
        j = 2
        while i * j <= N:
            prime[i*j] = 0
            j+=1
    i+=1

lst=[]
for i in range(2,N+1):
    if prime[i]:
        lst.append(i)

# two pointer
answer = 0
if lst:
    i,j = 0,0
    value = lst[i]
    while 0 <= i <= j:
        if value < N:
            j+=1
            if j >= len(lst): break
            value += lst[j]
            
        elif value > N:
            value -= lst[i]
            i+=1
        else: # value == N
            answer+=1
            j+=1
            if j >= len(lst): break
            value += lst[j]

print(answer)