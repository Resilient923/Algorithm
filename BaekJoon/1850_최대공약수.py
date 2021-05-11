import sys
input = sys.stdin.readline
n,m = map(int,input().split())

if(m>n): 
    n,m = m,n

#최대공약수를 구하는 유클리드 호제법
#큰 수를 작은 수로 나누어 구한 나머지로 큰 수를 대체한다. 큰 수를 작은 수로 계속 나누어서 나누어 떨어질 때까지 반복한다.
while(m!=0):
  n=n%m
  n,m=m,n


print(''.join(['1']*n))
