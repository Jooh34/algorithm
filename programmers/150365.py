# def solution(n, m, x_, y_, r, c, k):
#     # dlru

#     q = [(x_,y_,0,"")] # x, y, d, route
#     while q:
#         x, y, d, route = q.pop(-1)

#         if abs(x-r) + abs(y-c) > k-d:  # ignore impossible
#             continue

#         if d == k:
#             if x == r and y == c:
#                 return route
#             else:
#                 continue
        
#         if x-1 > 0: #u
#             q.append((x-1, y, d+1, route+"u"))
#         if y+1 <= m: #r
#             q.append((x, y+1, d+1, route+"r"))
#         if y-1 > 0: #l
#             q.append((x, y-1, d+1, route+"l"))
#         if x+1 <= n: #d
#             q.append((x+1, y, d+1, route+"d"))

#     return 'impossible'


def solution(n, m, x, y, r, c, k):
    dist = 0

    answer = ''
    while dist < k:
        # can go d?
        new_x = x+1
        if new_x <= n and abs(r-new_x) + abs(c-y) <= (k-dist):
            answer += 'd'
            dist += 1
            x = new_x
            continue

        new_y = y-1
        if new_y > 0 and abs(r-x) + abs(c-new_y) <= (k-dist): # l
            answer += 'l'
            dist += 1
            y = new_y
            continue

        new_y = y+1
        if new_y <= m and abs(r-x) + abs(c-new_y) <= (k-dist): # r
            answer += 'r'
            dist += 1
            y = new_y
            continue

        new_x = x-1
        if new_x > 0 and abs(r-new_x) + abs(c-y) <= (k-dist):
            answer += 'u'
            dist += 1
            x = new_x
            continue

        break

    if x == r and y == c:
        return answer
    else:
        return 'impossible'

q1 = [3,	4,	2	,3	,3	,1,	5]
print(solution(*q1))