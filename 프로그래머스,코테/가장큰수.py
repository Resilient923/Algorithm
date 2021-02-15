""" def solution(numbers):
    data = []
    for i in numbers:

    answer = ''
    return answer """

numbers = [6,10,2]

data = []
answer= []
for i in numbers:
    while (i != 0):
        data.append(i%10)
        i = (i//10)
for i in data:
    answer.append(str(i))

answer.sort(reverse=True)
a = ("".join(answer))

print('\"'+a+'\"')