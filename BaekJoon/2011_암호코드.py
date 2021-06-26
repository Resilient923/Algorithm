import sys
input = sys.stdin.readline

data = list(map(int,input().rstrip()))
len_data = len(data)
dp = [0] * (len_data+1)
if data[0] == 0:
    print(0)
    exit(0)
else:
    # 인덱스맞추기 위한 0 삽입
    data = [0] + data
    # 1까지는 만들 수 있는 글자 1개
    dp[0] = 1
    dp[1] = 1
    for i in range(2,len_data+1):
        # 앞자리숫자와 그 다음 숫자가 26이하의 두자리 숫자라고 가정
        if 10 <= data[i-1]*10 + data[i] <= 26:
            # i번째 dp에 앞앞 자리 까지의 dp값을 더해준다. -> 두자리숫자 한개로 친다.
            dp[i] += dp[i-2]
        # 한자리 숫자라고 가정
        if 1 <= data[i] <= 9:
            # 하나 앞자리 숫자의 dp값을 더해준다.
            dp[i] += dp[i-1]
        dp[i] %= 1000000
print(dp[len_data])

