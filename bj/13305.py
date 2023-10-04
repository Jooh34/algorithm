import sys
input = sys.stdin.readline
N = int(input())

answer = 0
road = list(map(int,input().split()))
cost = list(map(int,input().split()))

cur_i = 0

i = 1
find = -1
while i < N:
    if cost[cur_i] > cost[i]: # cheaper gas station
        find = i
        answer += sum(road[cur_i:i]) * cost[cur_i]
        cur_i = i
    i+=1

answer += sum(road[cur_i:i]) * cost[cur_i]
print(answer)