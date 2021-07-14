import sys
input = sys.stdin.readline
#from itertools import permutations

n = int(input())
data = list(map(int,input().split()))
flag = 0
for i in range(n-1,0,-1):
    if data[i-1] < data[i]:
        for j in range(n-1,0,-1):
            if data[i-1] < data[j]:
                data[i-1],data[j] = data[j],data[i-1]
                ans = data[:i]+sorted(data[i:])
                flag = 1
                break
    if flag == 1:
        print(*ans)
        break
else:
    print(-1)
    
# num = [i for i in range(1,n+1)]
# num_permutations = list(permutations(num,n))

# for i in range(len(num_permutations)):
#     if list(num_permutations[i])== data:
#         if i == len(num_permutations)-1:
#             print(-1)
#         else:
#             for i in num_permutations[i+1]:
#                 print(i,end=" ")

##permutations 쓰면 메모리초과, 시간초과


