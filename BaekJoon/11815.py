#처음작성한 코드 시간초과
import sys
""" n = int(sys.stdin.readline())
n_data=(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_data=(list(map(int,sys.stdin.readline().split())))
dp = [0 for i in range(m)]
for i in range(len(m_data)):
    for j in range(len(n_data)):
        if (m_data[i]==n_data[j]):
            dp[i]=1
print(dp) """
#두번째코드
n = int(sys.stdin.readline())
n_data=set(map(int,input().split()))
m = int(sys.stdin.readline())
m_data=(list(map(int,sys.stdin.readline().split())))
for i in m_data:
    if i in n_data:
        print(1, end=' ')
    else:
        print(0, end=' ')
