def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        n1 = arr1[i]
        n2 = arr2[i]
        result = ''

        bit_or = n1 | n2
        for j in range(n):
            if bit_or % 2:
                result = '#' + result
            else:
                result = ' ' + result
            bit_or = bit_or >> 1

        answer.append(result)
    return answer

n=	6
arr1=	[46, 33, 33 ,22, 31, 50]
arr2=	[27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
