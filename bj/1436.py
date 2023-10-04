n = int(input())

find = 0
i = 666
while True:
    stri = str(i)
    six = 0
    for s in stri:
        if s == '6':
            six += 1
            if six == 3:
                find+=1
                break
        else:
            six = 0

    if find == n:
        print(i)
        break
    
    i+=1