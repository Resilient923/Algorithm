n = int(input())
data = list(map(int,input().split()))

cnt =0
for i in data:
    if i !=1:
        if i ==2:
            cnt+=1
        elif i == 3:
            cnt +=1
        elif (i+1)%6==0:
            cnt+=1
        elif(i-1)%6==0:
            cnt+=1
    
print(cnt)
    
    
    
    