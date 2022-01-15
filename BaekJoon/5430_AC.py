import sys,re
from collections import deque

input = sys.stdin.readline


# 1. deque reverse 와 deque.popleft() 사용
# 2. reverse를 사용은 하되 어떻게 최소화 할 수 있을지?
t= int(input())
for _ in range(t):
    p = str(input())
    num = int(input())
    # 문자열로 들어오기 때문에 마지막 괄호와 , 를 제외한  숫자 문자를 파싱해준다.
    number = deque(input().rstrip()[1:-1].split(","))
    # 0일 때는 아무것도 안넣은 리스트를 만들어준다.
    if num == 0:
        number = deque([])
    # 수행할 조건을 담은 deque를 만들어준다.
    p_q = deque(list(p.rstrip()))
    # R이 홀수이면 0 짝수이면 1이 되도록 flag를 만들어준다.
    flag = 0
    # 위에서 num이 0일 경우 error를 출력하기 위한 flag 
    empty_flag = 0
    while p_q:
        i = p_q.popleft()
        if i == 'D':
            if  not number:
                empty_flag = 1
            # flag 가 1이면 리스트 오른쪽 제거 ( 이후에 reverse 예정)
            elif number and flag == 1:
                number.pop()
            # flag 가 0 이면 리스트 왼쪽 제거 ( 이후에 reverse 안할 예정)
            elif number and flag == 0:
                number.popleft() 
        # 두번 바뀌면 안뒤집어 줘도 되고 빼주는 위치만 고려해주면된다.
        # 나중에 한꺼번에 Reverse 해야 시간초과가 발생하지 않는다.
        elif i == 'R' and flag == 0:
            flag = 1
        elif i == 'R' and flag == 1:
            flag = 0
        
    if empty_flag == 1:
        print("error")
    else:
        if flag == 1:
            number.reverse()
        # number에 str 형태로 들어가 있기 때문에 join을 해준다.
        print("[", end = "") 
        print(",".join(number), end = "") 
        print("]")


