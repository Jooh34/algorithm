N = int(input())

lst = [[' ']*N for _ in range(N)]

def star(i,j,l):
    if l == 1:
        lst[i][j] = '*'
        return

    nl = l//3
    for ni in range(3):
        for nj in range(3):
            if ni==1 and nj==1:
                continue
                
            star(i+ni*nl, j+nj*nl, nl)

star(0,0,N)

for i in range(N):
    print(''.join(lst[i]))