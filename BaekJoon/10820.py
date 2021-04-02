import sys
input = sys.stdin.readline

while True:
    data = input().rstrip('\n')
    if not data:
        break
    
    a,b,c,d =0 ,0,0,0
    for i in data:
        if ord(i)>=48 and ord(i)<=57:
            c += 1
        elif ord(i)>=65 and ord(i)<=90:
            b +=1
        elif ord(i)>=97 and ord(i)<=122:
            a += 1
        elif i == ' ':
            d += 1
    print(a,b,c,d)