import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

#중간값을 구성


""" data = []
for i in range(n):
    for j in range(m):
        data.append(graph[i][j])
data = list(set(data))
num_list = []
for i in data:
    cnt = 0
    for j in range(n):
        for k in range(m):
            if i==graph[j][k]:
                cnt+=1
    num_list.append((i,cnt))
num_list.sort(key=lambda x:x[1])
num_min = num_list[0][0]
num_max = num_list[-1][0]
if num_list[0][1] <= b:
    if num_min < num_max:
        print(num_list[0][1],num_max)
    else:
        print(num_list[0][1]*2,num_max)
else:
    print(num_list[-1][1]*2,num_min) """

