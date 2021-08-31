import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

list_n = [i for i in range(1,n+1)]
data = list(permutations(list_n,n))
for i in data:
    print(*i)