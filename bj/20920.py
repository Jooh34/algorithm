from collections import defaultdict

N,M = map(int, input().split())
d = defaultdict(int)
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    
    d[word] += 1

lst = []
for k,v in d.items():
    lst.append((-v,-len(k), k))

lst.sort()
answer = [s for _,_,s in lst]
print('\n'.join(answer))
