n = int(input())
graph =[]
for _ in range(n):
    graph.append(list(map(int,input())))
cnt =0
answer=[]
def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        cnt += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(n):
        cnt=0
        if dfs(i,j) == True: 
            answer.append(cnt)
            result += 1
print(result)

for i in sorted(answer):
    print(i)
