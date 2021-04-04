import sys
input = sys.stdin.readline
data = input().split('-')
ans = 0
#-가 처음으로 나오고 뒤에 다 더하면된다.
for i in data[0].split('+'):
    ans += int(i)
for i in data[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)
print(data)
 