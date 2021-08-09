


def solution(price, money, count):
    answer = -1
    num = 0
    for i in range(1,count+1):
        num += price *i
    answer = (num - money) if num >=money else 0



    return answer


price = 3
money = 20
count = 4



print(solution(price,money,count))