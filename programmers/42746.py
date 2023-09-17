from functools import cmp_to_key

def compare(a, b):
    temp_a = int(a)
    temp_b = int(b)
    if len(a) == 1:
        temp_a = int(a+a+a)
    elif len(a) == 2:
        temp_a = int(a+a[1])
    elif a == '1000':
        temp_a = 0.5

    if len(b) == 1:
        temp_b = int(b+b+b)
    elif len(b) == 2:
        temp_b = int(b+b[1])
    elif b == '1000':
        temp_b = 0.5

    if temp_a < temp_b:
        return -1
    elif temp_a > temp_b:
        return 1
    else:
        return 0


def solution(numbers):
    n = [str(x) for x in numbers]

    sorted_n = sorted(n, key=cmp_to_key(compare), reverse=True)
    print(sorted_n)
    return "".join(sorted_n)

# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([345, 33, 3, 35, 354, 1000]))
# print(solution([987, 98, 97, 9, 8, 90, 99, 0, 0, 10, 11, 12, 1, 111, 110, 112, 120]))
# print(solution([10, 101, 1, 100, 1000]))
print(solution([555, 565, 566, 55, 56, 5, 54, 544, 549]))