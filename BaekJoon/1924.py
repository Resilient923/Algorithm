import sys
input = sys.stdin.readline

x,y = map(int,input().split())

days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

month31 = [1,3,5,7,8,10,12]
month30 = [4,6,9,11]
month28 = [2]

date = 0
for i in range(1,x):
    if i in month31:
        date += 31
    elif i in month30:
        date+=30
    else:
        date += 28
date += y
print(days[date%7])