import sys
input = sys.stdin.readline

h,w = map(int,input().split())

block = list(map(int,input().split()))
rains = 0
for i in range(1, w - 1):
    
    max_leftheight = block[i]
    for j in range(i - 1, -1, -1):
        if max_leftheight < block[j]:
            max_leftheight = block[j]
    
    max_rightheight = block[i]
    for j in range(i + 1, w):
        if max_rightheight< block[j]:
            max_rightheight =block[j]
    max_height = min(max_leftheight, max_rightheight)
    rains += max_height - block[i]

print(rains)