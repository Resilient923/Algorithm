import sys

n,m = map(int,sys.stdin.readline().split())
look = []
hear = []
lookhear =[]
for _ in range(n):
    look.append(sys.stdin.readline().strip())
for _ in range(m):
    hear.append(sys.stdin.readline().strip())
lookhear = list(set(look) & set(hear))
print(len(lookhear))
for i in sorted(lookhear):
    print(i) 
