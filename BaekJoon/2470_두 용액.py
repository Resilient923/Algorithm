import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

n = int(input())
# 값들을 입력받는다.
data = list(map(int,input().split()))
# 정렬을 일단한다. 이분탐색 사용해야한다.
data.sort()

start  = 0
end = n-1

# 계속해서 최솟값을 갱신해줘야 하기 때문에 Min을 설정해준다.
Min = 10000000000
print(data)
while start < end:
    first_line = data[start]+data[end]
    if abs(first_line) <= abs(Min):
        Min = first_line
        s,e = data[start],data[end]
    # 여기서는 first_line 이 mid 라고 생각하면 된다
    if first_line == 0:
        break
    elif first_line > 0:
        end -= 1
    elif first_line <0:
        start += 1
print(s,e)


# mid 가 뭐야? 두개의 용액으로 만들수있는 최소.
# mid를 만들어 내는 두개의 용액을 구하는게 문제

# 투 포인터를 사용
# 양 끝값에서 시작해서 하나하나 넘어오면서 비고해서 
# mid값이 나오는지 비교

# 시간초과
# Min = 1000000000
# end = 0
# for start in range(n):
#     # end 를 이동하면서 최솟값을 갱신
#     while end<n-1:
#         num = data[start] + data[end]
#         result = abs(0-num)
#         if Min > result:
#             Min = result
#             answer.append((Min,data[start],data[end]))
#         end += 1
# answer.sort(key=lambda x:x[0]   )
# ans = list(answer[0][1:])
# ans.sort()
# print(ans)
    
# 1. 힙 정렬로 오름차순
# 2. mid를 구하는게 아니라 어쨌든 다 비교해줘야하는데
# 3. mid를 끝낼 기준이 필요한데, 최솟값이면 갱신을 계속 해줘야한다.




    

