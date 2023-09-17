MAX = 360001
def stamp_to_sec(stamp):
    h,m,s = map(int,stamp.split(':'))
    return h*3600+m*60+s

def sec_to_stamp(sec):
    h = sec // 3600
    sec = sec % 3600
    m = sec // 60
    s = sec % 60

    h = '0'+str(h) if h < 10 else str(h) 
    m = '0'+str(m) if m < 10 else str(m) 
    s = '0'+str(s) if s < 10 else str(s) 
    return "{}:{}:{}".format(h,m,s)

def solution(play_time, adv_time, logs):
    accum = [0]*MAX
    for log in logs:
        start_end = []
        for t in log.split('-'):
            start_end.append(stamp_to_sec(t))
        
        accum[start_end[0]] += 1
        accum[start_end[1]] += -1

    for i in range(MAX-1):
        accum[i+1] += accum[i]

    pt = stamp_to_sec(play_time)
    adt = stamp_to_sec(adv_time)

    start = 0
    end = adt

    print(accum[30*3600-1])
    time = sum(accum[start:end])
    max_ = time
    answer = start
    while end <= pt:
        if max_ < time:
            max_ = time
            answer = start
        time -= accum[start]
        time += accum[end]
        start+=1
        end+=1
        

    print(max_)
    return sec_to_stamp(answer)

q1 = ["02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]]
q2 = ["50:00:00"	,"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]
q3 = ["50:00:00"	,"30:00:00",	["49:59:59-50:00:00"]]
print(solution(*q3))