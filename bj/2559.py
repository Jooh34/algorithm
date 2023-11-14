N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0]+lst

prefix = [0]*(N+1)
for i in range(1,N+1):
    prefix[i] = lst[i]+prefix[i-1]

answer = -1000000000
for i in range(K,N+1):
    #i i-K
    v = prefix[i]-prefix[i-K]
    answer = max(answer, v)
    
print(answer)
