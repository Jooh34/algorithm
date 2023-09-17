def solution(tickets):
    len_tickets = len(tickets)
    ap_list = sorted(list(set(sum(tickets, []))))
    dic = {}
    for i, air_list in enumerate(ap_list):
        dic[air_list] = i
    
    dg = [[[]] * len(ap_list) for _ in range(len(ap_list))]
    for i, (f, t) in enumerate(tickets):
        dg[dic[f]][dic[t]] = dg[dic[f]][dic[t]] +[i]
    
    start = dic["ICN"]
    q = [(start, [start], [])] # start, root, used
    while q:
        ap, root, used = q.pop()
        if len(root) == len_tickets+1:
            return list(map(lambda x : ap_list[x], root))

        for i in range(len(ap_list)-1, -1, -1):
            if dg[ap][i]:
                for t in dg[ap][i]:
                    if t not in used:
                        q.append((i, root + [i], used + [t]))
        

q1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
q2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
q3 = [["ICN", "AAZ"], ["AAZ", "AAF"], ["AAF", "AAC"], ["AAC", "ABA"], ["ABA","ICN"]]
print(solution(q1))
print(solution(q2))
print(solution(q3))