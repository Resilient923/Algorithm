import sys
input = sys.stdin.readline

n = int(input())
graph =[list(input()) for _ in range(n)]

result = []
def function(x,y,length):
    #한 압축영상의 시작 값을 start로 둔다.
    start = graph[x][y]
    for i in range(x,x+length):
        for j in range(y,y+length):
            #start (쪼개진 첫번째 값) 과 다르면
            if start != graph[i][j]:
                #쪼개짐이 시작되는 경우에 ( 를 넣어주고
                result.append("(")
                # 4개로 쪼개준다.
                for a in range(2):
                    for b in range(2):
                        function(x+length//2*a,y+length//2*b,length//2)
                #다 처리해준뒤에는 ) 로 닫아준다
                result.append(")")      
                #처리해주고 리턴
                return
    print(x,y)
    #여기서부터는 쪼개질대로 쪼개지고, start값과 같은 것만
    #start 가 0이면 0넣어주고
    if start == '0':
        result.append(0)
    #start가 1이면 1넣어준다.
    elif start == '1':
        result.append(1)
function(0,0,n)
for i in result:
    print(i,end="")