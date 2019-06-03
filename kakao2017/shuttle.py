def solution(n, t, m, timetable):
    answer = ''

    timetable = sorted(timetable, key=lambda time: int(time.replace(':', '')))
    
    return answer


timetable = ['09:10', '09:09', '08:00', '08:01']
n = 2
t = 10
m = 2

print(solution(n, t, m, timetable))
