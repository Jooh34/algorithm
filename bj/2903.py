N = int(input())

n = 3
for i in range(N-1):
    n += 2**(i+1)
print(n**2)