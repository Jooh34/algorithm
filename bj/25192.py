N = int(input())

answer = 0
_set = set()
for _ in range(N):
    s = input()
    if s == 'ENTER':
        _set.clear()
    else:
        if s not in _set:
            answer+=1
            _set.add(s)

print(answer)
