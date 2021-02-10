Input = input()
i=0
while True:
    if i>=len(Input):
        break
    if Input[i:i+4]=='XXXX':
        i=i+4
        Input=Input.replace('X','A',4)
    elif Input[i:i+2]=='XX':
        i=i+2
        Input=Input.replace('X','B',2)
    elif Input[i]=='.':
        i=i+1
    else:
        Input=-1
        break
print(Input)
