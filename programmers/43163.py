def solution(begin, target, words):
    li = [begin, *words]
    if target in li:
        li.remove(target)
        li.append(target)
    else:
        return 0

    g = [[0] * len(li) for _ in range(len(li))]

    for i, w1 in enumerate(li):
        for j, w2 in enumerate(li):
            if i == j: continue
            diff = 0
            for k in range(len(w1)):
                if w1[k] != w2[k]: diff += 1
            
            if diff == 1:
                g[i][j]=1
    
    visited = [False] * len(li)
    q = [[0, 0]]
    while q:
        x, d = q.pop(0)
        if visited[x]: continue
        visited[x] = True
        # print(x, d)

        if x == len(li)-1:
            return d

        for i in range(len(li)):
            if g[x][i] == 1 and not visited[i]:
                # print(x, "->", i)
                q.append([i,d+1])
            
    return 0

q1 = ["hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"]]
q2 = ["hit","cog",["hot", "dot", "dog", "lot", "log"]]
print(solution(*q1))
print(solution(*q2))