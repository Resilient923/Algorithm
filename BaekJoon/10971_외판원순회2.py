import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

n_num = [i for i in range(n)]

def function(List):
    ans = 0
    for i in range(n-1):
        if data[List[i]][List[i+1]] != 0:
            ans += data[List[i]][List[i+1]]
        else:
            return False
        
    if data[List[-1]][List[0]] == 0:
        return False
    else:
        ans += data[List[-1]][List[0]]
    
    return ans

ans = 987654321
for List in permutations(n_num):
    result = function(List)
    if result != False:
        if ans > result:
            ans = result
print(ans)