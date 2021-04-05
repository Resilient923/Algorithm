import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_ = list(map(int,input().split()))
m = int(input())
m_ = list(map(int,input().split()))
n_ = Counter(n_)
for i in m_:
    print(n_[i],end=" ")


