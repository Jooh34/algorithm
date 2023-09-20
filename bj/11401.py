MOD = 1000000007
n,k = map(int,input().split())
A = B = 1 # A = n!, B = k!(n-k)!
for i in range(n):
    A*=(i+1)
    A%=MOD
for i in range(k):
    B*=(i+1)
    B%=MOD
for i in range(n-k):
    B*=(i+1)
    B%=MOD

exponent = MOD-2
B2 = 1
while exponent:
    if exponent % 2 == 1:
        B2 *= B
        B2 %= MOD
        exponent-=1
        continue
        
    B *= B
    B %= MOD
    exponent /= 2

print((A*B2) % MOD)