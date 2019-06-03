def solution(relation):
    def valueList(tuple, col):
        output = []
        for i in col:
            output.append(tuple[i])
        return output

    def isSuperKey(relation, col):
        for i, tuple in enumerate(relation):
            value1 = valueList(tuple, col)
            for j in range(i):
                value2 = valueList(relation[j], col)
                if value1 == value2:
                    return False

        return True

    def isSubset(s1, s2):
        for idx1 in s1:
            has = False
            for idx2 in s2:
                if idx1 == idx2:
                    has = True
                    break

            if not has:
                return False

        return True

    num_col = len(relation[0])
    super_key = []
    for count in range(1,2**num_col):
        set = []
        for j in range(num_col):
            if (count >> j) % 2:
                set.append(j)

        if isSuperKey(relation, set):
            output = []
            for i in set:
                output.append(i)
            super_key.append(output)

    super_key = sorted(super_key, key=lambda m: len(m))
    answer = 0
    for i in range(len(super_key)):
        if len(super_key[i]) == 1:
            answer+=1
            continue

        isDupl = False
        for j in range(0, i):
            if isSubset(super_key[j], super_key[i]):
                isDupl = True

        if not isDupl:
            answer+=1

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
