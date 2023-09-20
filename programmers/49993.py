def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        impossible = False
        s = list(skill)
        lst = list(skill_tree)
        for el in lst:
            if el in s:
                if el == s[0]:
                    s = s[1:]
                else:
                    impossible = True
                    break
        if impossible:
            continue
        else:
            answer += 1
    return answer

q1 = ["CBD",["BACDE", "CBADF", "AECB", "BDA"]]
print(solution(*q1))