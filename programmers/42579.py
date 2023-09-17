def solution(genres, plays):
    dic = {}

    for i, g in enumerate(genres):
        p = plays[i]
        if not g in dic:
            dic[g] = [p, [[p, i], [-1,-1]]]
        else:
            dic[g][0] += p
            tu = dic[g][1]
            if tu[1][1] == -1:
                if tu[0][0] < p:
                    tu[1] = tu[0]
                    tu[0] = [p,i]
                else:
                    tu[1] = [p,i]
            else:
                if tu[0][0] < p:
                    tu[1] = tu[0]
                    tu[0] = [p,i]
                elif tu[1][0] < p:
                    tu[1] = [p,i]
                    
    sor = sorted(dic.items(), key=lambda item: item[1][0], reverse=True)
    

    answer = []
    for _,v in sor:
        if v[1][0][1] != -1:
            answer.append(v[1][0][1])
        if v[1][1][1] != -1:
            answer.append(v[1][1][1])

    return answer

g = ["classic", "pop", "classic", "classic", "pop", "pop", "classic"]	
p = [500, 600, 150, 800, 2500, 500, 4000]
print(solution(g, p))