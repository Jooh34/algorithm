N = int(input())

answer = 0
_set = set()
_set.add("ChongChong")

for _ in range(N):
    a,b = input().split()

    if a in _set or b in _set: # dance
        _set.add(a)
        _set.add(b)

print(len(_set))
