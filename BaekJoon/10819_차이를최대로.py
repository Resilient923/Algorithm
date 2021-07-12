import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

data_list = list(permutations(data,n))
result = 0
for i in range(len(data_list)):
    ans = 0
    for j in range(1,len(data_list[i])):
        ans += abs(data_list[i][j-1] - data_list[i][j])
    result = max(ans,result)

print(result)