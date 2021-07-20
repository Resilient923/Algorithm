import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)
n = int(input())
graph = list(map(int,input().split()))
del_node = int(input())

tree = [[] for _ in range(n+2)]
for i in range(n):
    if graph[i] == -1:
        tree[n+1].append(i)
    else:
        tree[graph[i]].append(i)
def dfs(x):
    global cnt
    # tree[x]가 빈 리스트이면 자식 노드가 없다는 뜻 -> 리프노드라는뜻
    if len(tree[x]) == 0:
        cnt += 1
        return cnt
    for i in range(len(tree[x])):
        if tree[x][i] == del_node:
            # 만약에 원소가 하나라면 del_node랑 같을경우 del_node자식 노드를 다지우면 
            # del_node 부모노드라 리프노드가 되니까 +1 해준다.
            if len(tree[x]) == 1:
                cnt += 1
                return cnt
            else:
                continue
        else:
            dfs(tree[x][i])

cnt = 0
if graph[del_node] == -1:
    print(0)
else:
    # dfs(0)으로 계속 시도헀었는데 틀렸던 이유는
    # 처음 -1인 노드가 0번째가 아닐수도 있기 때문이다.
    dfs(n+1)
    print(cnt)
