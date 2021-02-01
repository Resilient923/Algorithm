N,K = map(int,input().split())
coin =[]
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
result = 0
for i in coin:
    result += K//i
    K %= i
print(result)
