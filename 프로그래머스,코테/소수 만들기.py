""" import math

# 에라토스테네스
# 2부터 소수 구하려는 범위까지 모든 수나열
# 2부터 시작해서 나열된 수에서 False가 아닌 수 중 가장 작은 2를 시작으로 선택하고 자기자신(2뺴고) 2의배수 싹지움
# 3도안지워졌으면 3빼고  3의배수 싹지움
# 4는 2에서 지워졌으니까 넘어가고
# 계속 반복 하면 배수인거는 일단 다 빠짐 -> 소수만 남음
n = 100
a = [True] * (n+1)

for i in range(2,int(math.sqrt(n))+1):
    if a[i] == True:
        for j in range(i*2,n+1,i):
            a[j] = False
print([i for i in range(2,n+1) if a[i] == True])
 """
 
from itertools import combinations
nums = [1,2,3,4]
comb = list(combinations(nums,3))
comb_sum = [0 for _ in range(len(comb))]
for i in range(len(comb)):
    for j in comb[i]:
        comb_sum[i]+=j
print(comb_sum)
def primenum(n):
    temp = 0
    #소수인지아닌지판별
    for i in range(2,n):
        if n % i ==0:
            temp = 1
    return temp
cnt = 0
for i in comb_sum:
    if primenum(i) == 0:
        cnt +=1
print(cnt)



