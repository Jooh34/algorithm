from collections import defaultdict
def solution(msg):
    answer = []

    table = defaultdict(int)
    ascii = ord('A')
    while ascii <= ord('Z'):
        table[chr(ascii)] = ascii-ord('A')+1
        ascii+=1

    table_key = ascii-ord('A')+1
    max_num = 1

    i=0
    while i < len(msg):
        for j in range(max_num, 0, -1):
            key = msg[i:i+j]
            if table[key] > 0:
                answer.append(table[key])
                if len(msg) <= i+j+1:
                    i+=j
                    break
                else: # find new table key
                    if max_num < j+1:
                        max_num = j+1

                    new_key = msg[i:i+j+1]
                    table[new_key] = table_key
                    table_key+=1
                
                i+=j
                break

    return answer

q1 = ['KAKAO']
q2 = ['TOBEORNOTTOBEORTOBEORNOT']
q3 = ['ABABABABABABABAB']
for q in [q1,q2,q3]:
    print(solution(*q))