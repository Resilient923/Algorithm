import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())

data = []
for _ in range(n):
    data.append(input().rstrip())
ans = list(set(list(permutations(data,k))))

result = set()
for i in ans:
    result.add("".join(i))
print(len(result))