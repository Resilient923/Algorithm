import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
_max = 0
for i in range(n):
    number = int(input())
    if number == 1:
        _max += number
    elif number >1:
        plus.append(number)
    else:
        minus.append(number)
plus.sort(reverse=True)
minus.sort()

for i in range(0,len(plus),2):
    if i+1<len(plus):
        _max += plus[i]*plus[i+1]
    else: #한개남으면 더한다
        _max += plus[i]
for i in range(0,len(minus),2):
    if i+1<len(minus):
        _max += minus[i]*minus[i+1]
    else: #한개남으면 더한다
        _max += minus[i]
print(_max)
