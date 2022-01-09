import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []
for i in range(1,n+1):
    ans.append(i)

student = defaultdict(list)
for i in range(m):
    student[i] =  list(map(int,input().split()))[1:]
result = []
for i in range(1,m+1):
    for j in list(combinations(student.keys(),i)):
        temp = []
        for k in j:
            temp.append(student[k])
        tmp = list(sum(temp,[]))
        tmp.sort()
        if (list(set(tmp))) == ans:
            result.append(j)
    
result.sort(key=len)
if result:
    print(len(result[0]))
else:
    print(-1)
