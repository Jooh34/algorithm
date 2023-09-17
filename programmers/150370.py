def expire(today, day, month):
    ty,tm,td = map(int, today.split('.'))
    dy,dm,dd = map(int, day.split('.'))
    dm += month

    dy += ((dm-1) // 12)
    dm = ((dm-1) % 12)+1
    
    if ty > dy : return True
    elif ty < dy : return False
    else:
        if tm > dm : return True
        elif tm < dm : return False
        else:
            if td >= dd : return True
            else: return False

def solution(today, terms, privacies):
    term_dic = {}
    for t in terms:
        a,b = t.split(' ')
        term_dic[a]=int(b)

    answer = []   
    for i, p in enumerate(privacies):
        d, t = p.split(' ')
        month = term_dic[t]
        v = expire(today, d, month)
        if v:
            answer.append(i+1)

    return answer


q1 = ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]]
q2 = ["2020.01.01", ["Z 3", "D 5"], ["2020.07.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]]
print(solution(*q1))
print(solution(*q2))