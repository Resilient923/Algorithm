n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited =[]

for i in range(m):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

count =[1]
while count:
    node1 = count.pop()
    visited.append(node1)
    for i in graph[node1]:
        if i not in visited+count:
            count.append(i)

print(len(visited)-1)