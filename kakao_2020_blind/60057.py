def solution(s):
    answer = 9999
    N = len(s)
    if N == 1:
        return 1
        
    for k in range(1,N//2+1):
        lst = []
        i = 0
        while i < N:
            lst.append(s[i:i+k])
            i+=k
        
        same_list = [1] * len(lst)

        cnt = 0
        for i in range(len(lst)):
            # next same
            if i+1 < len(lst) and lst[i+1] == lst[i]:
                same_list[i+1] = same_list[i]+1
                continue
            
            else: # next diff
                if same_list[i] > 1:
                    cnt += len(lst[i])+len(str(same_list[i]))
                else:
                    cnt += len(lst[i])

        answer = min(answer, cnt)
    return answer

ql =["a", "aa", "ab", "xababcdcdababcdcd"]
for q in ql:
    print(solution(q))