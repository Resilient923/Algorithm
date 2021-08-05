#시간초과 때문에 2중 for문은 안되고..
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
data = list(map(int,input().split()))

cursor_1 = 0
cursor_2 = 0
ans = 100001
sum_ = 0
while 1:
    if sum_ >= s:
        sum_ -= data[cursor_1]
        cursor_1 += 1
        if cursor_2-cursor_1+1 < ans:
            ans = cursor_2-cursor_1+1 
    else:
        if cursor_2 == n:
            break
        else:
            sum_ += data[cursor_2]
            cursor_2 += 1
if ans < 100001:
    print(ans)
else:
    print(0)   

# for i in range(n):
#     while sum_<s and cursor_2 < n:
#         sum_ += data[cursor_2]
#         cursor_2 += 1
#     if sum_ >= s:
#         if abs(cursor_2-cursor_1)+1 < ans:
#             ans = abs(cursor_2-cursor_1)+1   
#     sum_ -= data[cursor_1]
                        
