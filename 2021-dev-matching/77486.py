
def solution(enroll, referral, seller, amount):
    LEN = len(enroll)
    answer = [0] * LEN
    ref_table = {} # (int->int)

    name_table = {}
    for i,e in enumerate(enroll):
        name_table[e] = i

    for i,r in enumerate(referral):
        if r == '-': continue
        ref_table[i] = name_table[r]

    # dfs
    q = [] # (index, money)
    for sell, am in zip(seller, amount):
        next_ = (name_table[sell], am*100)
        while next_ != None:
            me, money = next_
            if ref_table.get(me) != None:
                ref = ref_table[me]
                give = money // 10

                answer[me] += (money-give)
                if give != 0:
                    next_ = (ref, give)
                else:
                    break
                
            else:
                give = money // 10 # to minho
                answer[me] += (money-give)
                break

    return answer


q1 = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10]]
print(solution(*q1))