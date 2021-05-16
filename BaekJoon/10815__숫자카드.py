#처음작성한 코드 시간초과
import sys
input = sys.stdin.readline
n = int(sys.stdin.readline())
n_data=(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_data=(list(map(int,sys.stdin.readline().split())))
dp = [0 for i in range(m)]
for i in range(len(m_data)):
    for j in range(len(n_data)):
        if (m_data[i]==n_data[j]):
            dp[i]=1
print(dp)
#두번째코드
n = int(input())
n_data=set(map(int,input().split()))
m = int(sys.stdin.readline())
m_data=(list(map(int,input().split())))
for i in m_data:
    if i in n_data:
        print(1, end=' ')
    else:
        print(0, end=' ')

#이진탐색풀이
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
m = int(input())
s_ = list(map(int, input().split()))
s.sort()
for i in s_:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if 0 <= mid < n:
            if s[mid] < i: 
                low = mid + 1
            else: 
                high = mid - 1
        else: 
            break
    if 0 <= high + 1 < n:
        if s[high + 1] == i: 
            print(1, end=" ")
        else: 
            print(0, end=" ")
    else:
         print(0, end=" ")
