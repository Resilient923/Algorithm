import sys
input = sys.stdin.readline

n = int(input())
graph =[list(map(int,input().split())) for _ in range(n)]

#-1,0,1 카운트를 저장함
minus_cnt = 0
zero_cnt = 0
one_cnt = 0
def function(x,y,length):
    global cnt,minus_cnt,zero_cnt,one_cnt
    for i in range(x,x+length):
        for j in range(y,y+length):
            #다른 수의 종이조각이 나왔을때
            if graph[x][y] != graph[i][j]:
                for a in range(3):
                    for b in range(3):
                        function(x+length//3*a,y+length//3*b,length//3)
                return
    # 다 같은수로 이루어진 종이조각일 때,
    print(x,y)
    if graph[x][y] == 0:
        zero_cnt += 1
    elif graph[x][y] == -1:
        minus_cnt +=1
    elif graph[x][y] == 1:
        one_cnt += 1
    
#9개로 자르려면 3 x 3 으로 나눠야한다.
function(0,0,n)
print(minus_cnt)
print(zero_cnt)
print(one_cnt)


