from itertools import permutations

numbers = "011"

numbers = list(numbers)

data = []
for i in range(len(numbers)):
    data += (list(map(''.join, permutations(numbers,i+1))))

data = set(list(map(int,data)))
data -= set(range(0,2))
for i in range(2, int(max(data) ** 0.5) + 1):
    data -= set(range(i * 2, max(data) + 1, i))
    #에라토스테네스 체
    #에라토스테네스 체란 n=2부터 시작하여 일정 범위까지 자신을 제외한 n의 배수를 삭제하면, 남아있는 수는 모두 소수가 된다는 법칙
len(data)
answer = 0

print(answer)
