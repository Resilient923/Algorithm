n = int(input())

for i in range(n):
    cnt = 0
    data = list(input())
    for j in data:
        if j =='(':
            cnt+=1
        elif j ==')':
            cnt-=1
        if cnt <0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    elif cnt == 0:
        print('YES')