a,b = map(int,input().split())
data=[]
for i in range(1,46):
    data +=[i]*i
    
print(sum(data[a-1:b]))