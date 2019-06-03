def solution(food_times, k):
    sorted_times = []
    for i, time in enumerate(food_times):
        sorted_times.append([time, i])

    sorted_times = sorted(sorted_times, key=lambda x: x[0])
    length = len(sorted_times)

    prev_n = 0
    answer = -1
    for i in range(length):
        if sorted_times[i][0] == prev_n:
            continue

        n = sorted_times[i][0]
        k = k - (length-i) * (n - prev_n)

        if k<0:
            k = k + (length-i) * (n - prev_n)
            remain = length - i
            new_list = sorted_times[i:]
            new_list = sorted(new_list, key=lambda x: x[1])
            answer = new_list[k % remain][1] + 1
            break

        prev_n = n

    return answer

food_times = [1, 3, 5]
k = 4
print(solution(food_times, k))
