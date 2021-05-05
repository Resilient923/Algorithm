import sys
input = sys.stdin.readline

#시간초과 코드
""" n = int(input())
schedule = []
for _ in range(n):
    start,end = map(int,input().split())
    schedule.append([start,end])
dp = [0 for _ in range(n+1)]
for i in range(len(schedule)):
    now = schedule[i][0]
    _end = schedule[i][1]
    for j in range(1,len(schedule)):
        if _end<schedule[j][0]:
            now = schedule[j][0]
            _end = schedule[j][1]
            dp[i] += 1
print(max(dp)+1) """
n = int(input())
schedule = []
for _ in range(n):
    start,end = map(int,input().split())
    schedule.append([start,end])
schedule = sorted(schedule,key=lambda x : x[0])
schedule = sorted(schedule,key=lambda x : x[1]) #이게 핵심이다.
end_ = 0
cnt = 0
for start_, end in schedule:
    if start_>=end_:
        cnt += 1
        end_ = end
print(cnt)