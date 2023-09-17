from heapq import heappush, heappop

def solution(jobs):
    jobs=sorted(jobs)

    heap = []
    job_top = 0
    task = 0
    sum_wait = 0

    for t in range(1000000):
        # pop jobs
        while job_top < len(jobs) and jobs[job_top][0] == t:
            _, dur = jobs[job_top]
            heappush(heap, dur)
            job_top+=1

        # pop new job
        if task==0 and heap:
            task = heappop(heap)

        # running
        if task != 0:
            sum_wait += (len(heap)+1)
            task-=1

        # termination
        if len(jobs) <= job_top and task == 0 and not heap:
            break

    answer = sum_wait // len(jobs)
    return answer

q1 = [[7, 8], [3, 5], [9, 6]]
print(solution(q1))