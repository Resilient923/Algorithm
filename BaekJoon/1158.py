n,k = map(int,input().split())

data = []
result = []
for i in range(1,n+1):
    data.append(i)

num =0
while(len(data)>0):   
    num = (num+(k-1))%len(data)
    result.append(str(data.pop(num)))
    
print("<%s>" %(", ".join(result))) 




