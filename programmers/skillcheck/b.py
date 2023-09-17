def check_possible(n):
    global graph
    v = [False]*n
    q = [0]
    while q:
        node = q.pop()
        for i in range(n):
            if graph[node][i] != -1 and not v[i]:
                v[i] = True
                q.append(i)
    
    for b in v:
        if b == False:
            return False
    
    return True

def solution(n, costs):
    global graph
    graph = [[-1]*n for _ in range(n)]
    bridge_sum = 0
    for fr,to,co in costs:
        graph[fr][to] = co
        graph[to][fr] = co
        bridge_sum += co

    sorted_cost = sorted(costs, key = lambda x : x[2], reverse=True)
    for x,y,z in sorted_cost:
        graph[x][y] = -1
        graph[y][x] = -1
        
        p = check_possible(n)
        if p:
            bridge_sum -= z
        else:
            graph[x][y] = z
            graph[y][x] = z

    return bridge_sum

q1 = [4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]]
print(solution(*q1))