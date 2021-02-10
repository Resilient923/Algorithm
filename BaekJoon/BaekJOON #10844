처음 생각한 방법   #n이 100일때는 정말 어마어마한 숫자가 나온다. 테스트케이스는 통과. 

n = int(input())
cnt = 0
for i in range(10**(n-1),10**n):  #이 부분을 DP로 풀면 될거 같다.

    a = i % 10
    b = i // 10
    if(i<10):
        cnt+=1
    if(i>=10):
        if(b-a==1):
            cnt+=1
        elif(a-b==1):
            cnt+=1
print(cnt)
------------------------------------------------------------------------
DP테이블 만들어서 푼 방법


n = int(input())

dp = [[0]*10 for i in range(n+1)] # dp 테이블 생성

for i in range(1,10):
    dp[1][i] = 1  #한자리숫자일때 개수 초기화
if n==1:
    print(sum(dp[1]))
else:
    for i in range(2,n+1):
        for j in range(10):
            if j==0:
                dp[i][j] = dp[i-1][j+1]
            elif j==9:
                dp[i][j] = dp[i-1][j-1]
            elif 1<=j<=8:
                dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

    print(sum(dp[n])%1000000000)
