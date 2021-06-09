import sys
input = sys.stdin.readline
data = input().split('-')
ans = 0
#-가 처음으로 나올 때까지  - 앞에 숫자들은 다 더해준다. 
for i in data[0].split('+'):
    ans += int(i)
# - 가 나온 뒤로는 -가 나오거나,
# + 가 나와도 어차피 괄호로 - 처리 해주면 되기 때문에 값을 다 빼준다.(최솟값이 나와야함)
for i in data[1:]:
    # - 처리는 안해줘도 된다 어차피 맨 앞에서 -로 끊어서 이미 다 양수처리
    for j in i.split('+'):
        ans -= int(j)
print(ans)
 