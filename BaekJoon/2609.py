import sys
input = sys.stdin.readline

a,b = map(int,input().split())

min_num = 0

for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        min_num = max(min_num,i)
    #max(data_a)최대공약수
#최소공배수
data_b = min_num*(a//min_num)*(b//min_num)
print(min_num)
print(data_b)
