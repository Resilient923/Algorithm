import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(input().rstrip())

flag = 0
cnt = 0
ans = 0
i = 0
while i < m-2:
    if s[i] == 'I':
        flag = 1
    else:
        i += 1
    if flag == 1:
        #I가 나오면 그뒤에 OI 가 몇개가 나오는지에 따라 다르다. N개가 나와야한다.
        if s[i+1] == 'O' and s[i+2] == 'I':
            cnt += 1
            if cnt == n:
                ans += 1
                #OI 개수맨 세어주기 위해서 cnt가 n개면 ans += 1 해주고 cnt 한개 빼준다.
                cnt -= 1
            i += 2
        else:
            # I가 나와도 OI 가 안나오면 다 초기화 해주고 다음 I 카운트로 넘어가준다.
            cnt = 0
            flag = 0
            i += 1
print(ans)
# 시간초과 코드
# num = n+(n+1)
# Pn = ""
# for i in range(1,num+1):
#     if i % 2 == 1:
#         Pn += "I"
#     elif i % 2 == 0:
#         Pn += "O"
# start = 0
# cnt = 0
# while start<m-num+1:
#     temp = ""
#     for i in range(start,start+num):
#         temp+=s[i]
#     if temp == Pn:
#         cnt+=1
#     start += 1
# print(cnt)