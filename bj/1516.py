from heapq import heappush, heappop

N = int(input())

graph = [[] for i in range(N+1)]
costs = [0 for i in range(N+1)]
in_degree = [0] * (N+1)
answer = [-1 for i in range(N+1)]

for i in range(1,N+1):
    lst = list(map(int, input().split()))
    costs[i] = lst[0]
    parents = lst[1:len(lst)-1]
    for parent in parents:
        graph[parent].append(i)

    in_degree[i] = len(parents)

pq = [] # (cost, index)

# add root node
for i in range(1,N+1):
    if in_degree[i] == 0:
        heappush(pq, (costs[i], i))
    
while pq:
    cost, idx = heappop(pq)
    answer[idx] = cost
    for g in graph[idx]:
        in_degree[g]-=1
        if in_degree[g] == 0:
            heappush(pq, (costs[g]+cost, g))

print(*answer[1:])
