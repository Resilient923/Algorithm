import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000000)
#dfs 문제
def dfs(x):
    global cnt,graph
    visited[x]=1
    team.append(x)
    people = graph[x]
    
    if visited[people]:
        if people in team:
            cnt.append(team[team.index(people):]) # people 순서 불러와서 사이클
        return
    else:
        dfs(people)




t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0]+list(map(int,input().split()))

    visited = [1]+[0]*n
    cnt = []
    for i in range(1,n+1):
        if(visited[i]==0):
            team=[]
            dfs(i)
    #n에서 사이클 개수 빼기
    print(n-len(cnt))








