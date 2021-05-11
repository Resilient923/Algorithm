import math
N = 11
stations = [4, 11]
W = 1
# 그리디 문제
def solution(n, stations, w):
    cnt = 0
    start = 0
    for i in range(len(stations)):
        leftside = stations[i] - w-1
        cnt += math.ceil((leftside -start)/((2*w)+1))
       
        start = stations[i]+w
    cnt += math.ceil((n -start)/((2*w)+1))
    return cnt

print(solution(N,stations,W))