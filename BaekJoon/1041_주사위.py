import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
result = 0
if n ==1 :
    data.sort()
    cnt = 0 
    for i in range(5):
        result += data[i]
else:
    Min = []
    #핵심코드
    Min.append(min(data[0],data[5]))
    Min.append(min(data[1],data[4]))
    Min.append(min(data[2],data[3]))
    Min.sort()
    one = Min[0]
    two = Min[0]+Min[1]
    three = Min[0]+Min[1]+Min[2]
    result = (two)*((n-1)*4+(n-2)*4) + (three)*4 + (n-2)**2*one + 4*(n-2)*(n-1)*one
print(result)

""" one = min(data)

Min = 50
three_list = [0,1,2,3,4,5]
three_list = list(combinations(three_list,3))
temp1 = []
for i in range(len(three_list)):
    if i == 2 or i == 3 or i==4 or i==6 or i==8 or i==9 or i==10 or i== 11 or i==13 or i==15 or i==16:
        continue
    else:
        temp1.append(three_list[i])
for i in temp1:
    q,w,e = i
    if Min > data[q]+ data[w] + data[e]:
        Min = data[q]+ data[w] + data[e]
three = Min

Min2 = 50
two_list = [0,1,2,3,4,5]
two_list = list(combinations(two_list,2))
temp2 = []
for i in range(len(two_list)):
    if i==4 or i == 7 or i== 9:
        continue
    else:
        temp2.append(two_list[i])
for i in temp2:
    a,b, = i
    if Min2 > data[a]+data[b]:
        Min2 = data[a]+data[b]
two = Min2  """
