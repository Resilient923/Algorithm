n = int(input())
data = list(map(int,input().split()))
""" if 1 in data:
    del data[0]
data = set(list(map(int,data)))

for i in range(2, int(max(data) ** 0.5) + 1):
    data -= set(range(i * 2, max(data) + 1, i))
print(len(data)) """
""" cnt =0
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
     """
def prime_number(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
cnt = 0
for i in data:
    if prime_number(i)==True:
        cnt +=1
print(cnt)
    
    
    