import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 1
    data = []
    for i in range(n):
        a,b = map(int,input().split())
        data.append([a,b])
    data.sort(key=lambda x:x[0])
    max_people_idx = data[0][1]
    # 문제 잘읽기... 순위다........
    for i in range(n):
        # data[i][0]로 정렬해서 for문으로 돌린다는거 자체가 i+1 번째 사람은 얼마든지 떨어질수있다. 
        # 근데 면접점수 data[i][1]값이 비교되는 대상보다 작게되면 살아남는 것이다.
        if max_people_idx > data[i][1]:
            cnt+=1
            max_people_idx = data[i][1]
    print(cnt)

""" data1 = sorted(data,key=lambda x: x[1],reverse=True)
    data2 = sorted(data1,key=lambda x: x[2],reverse=True)
    cnt = 0
    max_idx1,max_idx2 = data2[0][1],data2[0][2]
    for i in range(n):
        if data[i][1]<max_idx1 and data[i][2]<max_idx2:
            cnt+=1
    if cnt == n-1:
        print(cnt)
    else:
        print(n-cnt) """
