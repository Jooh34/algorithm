def solution(dartResult):
    def tokenize(dartResult):
        arr = []

        prev = 'O'

        num = ''
        bonus = ''
        option = ''

        for char in dartResult:
            if '0' <= char and char <= '9':
                if prev == 'N':
                    num = 10
                else:
                    if prev == 'O':
                        arr.append([num, bonus, option])
                    else:
                        arr.append([num, bonus, ''])

                    num = int(char)

                prev = 'N'

            elif char == '*' or char == '#':
                option = char
                prev = 'O'

            else:
                if char == 'S':
                    bonus = 1
                elif char == 'D':
                    bonus = 2
                else:
                    bonus = 3

                prev = 'B'

        if prev == 'O':
            arr.append([num, bonus, option])
        else:
            arr.append([num, bonus, ''])

        return arr

    answer = 0
    arr = tokenize(dartResult)
    arr = arr[1:]
    print(arr)

    prev = 0
    for score in arr:
        cur = pow(score[0], score[1])

        if score[2] == '*':
            cur = cur * 2
            prev = prev * 2

        if score[2] == '#':
            cur = (-1) * cur

        answer = answer + prev
        prev = cur

    answer = answer + cur
    return answer

print(solution('1D2S0T'))
