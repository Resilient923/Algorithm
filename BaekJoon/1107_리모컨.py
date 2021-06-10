import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(input().split())

# 리모컨으로 나올수있는 최솟값
result = 987654321

length = 0
# 완전탐색의 끝판왕. 숫자를 1000001까지 다 훑는다 -> 만들수있는숫자 -500000 ~ 500000 까지.
for number in range(1000001):
    # str 처리해서 하나하나 문자 처리해서 깨진 버튼인지 확인
    for j in str(number):
        if j in broken:
            # 깨진 버튼이면 for문 탈출.
            break
    # 안깨진 버튼들만 모였으면, 자릿수+현재비교중인숫자에서 n 값을 뺀 절댓값을 더해서 원래 값과 비교.
    else:
        result = min(result,len(str(number))+abs(number-n))
# 구해진 result 값하고, 최소가 될 수 있는 값하고 비교해준다. 
# (예를 들면 99 같은 경우 버튼 다 못쓰면 1만 빼주면되는 경우)
result = min(result,abs(100-n))
print(result)
##################################################################


from itertools import product

channel = input()
m = int(input())
buttons = list(str(i) for i in range(10))
if m > 0: 
    broken_buttons = list(input().split())
    for x in broken_buttons:
        buttons.remove(x)
    
if m == 10:
    print(abs(int(channel) - 100))

else:
    min_dist = abs(int(channel) - 100) 

    # 이동하고자 하는 채널의 길이만큼 모든 순열을 구해보자.
    button_permutations = []
    for i in range(1, len(channel) + 1):
        button_permutations = list(product(buttons, repeat = i ))


        # +, - 버튼만 눌러서 이동하는 거리
        for c in button_permutations:
            move_channel = ''.join(c)
            distance_by_jumping = abs(int(move_channel) - int(channel)) + len(move_channel)
            if distance_by_jumping <= min_dist:
                min_dist = distance_by_jumping
    
    if '0' in buttons and len(buttons) >= 2:
        n = buttons[1] + '0' * len(channel)
        if abs(int(channel) - int(n)) + len(channel) + 1 < min_dist:
            min_dist = abs(int(channel) - int(n)) + len(channel) + 1
    elif len(buttons) >= 1:
        n = buttons[0] * (len(channel) + 1)
        if abs(int(channel) - int(n)) + len(channel) + 1 < min_dist:
            min_dist = abs(int(channel) - int(n)) + len(channel) + 1
    
    print(min_dist)