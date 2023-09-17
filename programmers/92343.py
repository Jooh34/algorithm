from collections import defaultdict
def solution(info, edges):
    answer = 1

    n = len(info)
    memo = [[]] * pow(2,n) # (#sheep, #wolf), represent 2 digit

    graph = defaultdict(list)
    for fr,to in edges:
        graph[fr].append(to)

    print(graph)
    stack = [1] # memo_index, 0=>1 , 1=>2, 2=>4 ....
    memo[1] = [1,0]
    
    while stack:
        memo_index = stack.pop()

        i = 0
        while (memo_index >> i) > 0:
            if (memo_index >> i) % 2 == 1: # i-index node exist
                for conn in reversed(graph[i]):
                    if memo_index & (1 << conn) != 0: #visited already
                        continue

                    new_memo_index = memo_index | (1 << conn)
                    if len(memo[new_memo_index]) != 0: #visited
                        continue

                    sheep_wolf = memo[memo_index].copy()
                    sheep_wolf[info[conn]] += 1

                    if sheep_wolf[0] > sheep_wolf[1]:
                        memo[new_memo_index] = sheep_wolf.copy()
                        stack.append(new_memo_index)
                        # print('memo :', new_memo_index, memo_index, sheep_wolf)
                        if sheep_wolf[0] > answer: # max sheep num
                            answer = sheep_wolf[0]
                    
                    else:
                        pass

                
            i += 1
        
        # print(stack)
        
    return answer

q1 = [[0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]]
q2 = [[0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]]
q3 = [[0,1], [[0,1]]]
print(solution(*q3))