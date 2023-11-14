import sys
input = sys.stdin.readline

NUM_ALPHABET = 26
s = input().strip()
q = int(input().strip())

prefix = [[0]*(len(s)+1) for _ in range(NUM_ALPHABET)]

for i in range(1,len(s)+1):
    for alpha in range(NUM_ALPHABET):
        prefix[alpha][i] += prefix[alpha][i-1]
        
    ch = s[i-1]
    prefix[ord(ch)-ord('a')][i] += 1

for _ in range(q):
    alpha, l, r = input().split()
    alpha_idx = ord(alpha)-ord('a')

    v = prefix[alpha_idx][int(r)+1] - prefix[alpha_idx][int(l)]
    print(v)


