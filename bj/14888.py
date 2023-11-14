N = int(input())
lst = list(map(int, input().split()))
op_lst = list(map(int, input().split()))
MAX = 1_000_000_000
global _max, _min
_max = -MAX
_min = MAX

def btk(v, i, op_lst):
    global _max, _min
    if i == N:
        _max = max(_max, v)
        _min = min(_min, v)
        return

    #choose operator
    for j, rem in enumerate(op_lst):
        if rem == 0:
            continue
        else:
            if j == 0:
                new_v = v+lst[i]
            elif j == 1:
                new_v = v-lst[i]
            elif j == 2:
                new_v = v*lst[i]
            else:
                if v < 0:
                    new_v = -(-v//lst[i])
                else:
                    new_v = v//lst[i]

            op_lst[j] -= 1
            btk(new_v, i+1, op_lst)
            op_lst[j] += 1
            

btk(lst[0], 1, op_lst)

print(_max)
print(_min)