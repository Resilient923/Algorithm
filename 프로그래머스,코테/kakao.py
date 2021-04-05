#4
""" from collections import deque
def order(city_nodes, city_from, city_to, company):
    # Write your code here
   
    graph = [[]for i in range(city_nodes+1)]
    
    for i in range(len(city_from)):
        graph[city_from[i]].append(city_to[i])
        graph[city_to[i]].append(city_from[i])
        
        
    visited = [0]*(city_nodes+1)
    result = []
    q = deque([company])
    visited[company] = 1
    while q:
        v = q.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=1
    result.pop(0)
    return result

if __name__ == '__main__':
    

    city_nodes, city_edges = map(int, input().rstrip().split())

    city_from = [0] * city_edges
    city_to = [0] * city_edges

    for i in range(city_edges):
        city_from[i], city_to[i] = map(int, input().rstrip().split())

    company = int(input().strip())

    result = order(city_nodes, city_from, city_to, company)

    print('\n'.join(map(str, result)))
    print('\n')
 """
#1
def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    # Write your code here

    graph = [[]*rows for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
             while(graph[i][j]):
                for i in range(rows):
                    if i>0:
                        result += costRows[i-1]
                    for j in range(cols):
                        if j>0:
                            result += costCols[j-1]
                    if i ==finalR and j == finalC:
                        break
                    
    return result
        
        
if __name__ == '__main__':
    

    rows = int(input().strip())

    cols = int(input().strip())

    initR = int(input().strip())

    initC = int(input().strip())

    finalR = int(input().strip())

    finalC = int(input().strip())

    costRows_count = int(input().strip())

    costRows = []

    for _ in range(costRows_count):
        costRows_item = int(input().strip())
        costRows.append(costRows_item)

    costCols_count = int(input().strip())

    costCols = []

    for _ in range(costCols_count):
        costCols_item = int(input().strip())
        costCols.append(costCols_item)

    result = minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols)

    print(str(result) + '\n')
for i in range(rows):
    if i>0:
        result += costRows[i-1]
    for j in range(cols):
        if j>0:
            result += costCols[j-1]
  #  if i == finalR and j == finalC:
   