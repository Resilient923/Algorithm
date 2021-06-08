import sys
input = sys.stdin.readline

# \n를 빼주기 위해서 restrip() 을 사용
data = list(input().rstrip())

stack = []

for i in data:
    if i ==')':
        flag = 0
        while len(stack)>0:
            compare_pop = stack.pop()
            if compare_pop == '(':
                # 바로 옆에 ( 가 있을 때
                if flag == 0:
                    stack.append(2)
                else:
                    stack.append(2*flag)
                # 짝을 한번 찾으면  break로 while문 빠져나가준다.
                break
            # 잘못된 괄호열
            elif compare_pop == '[':
                print(0)
                # 인자값이 0이 들어가면 종료해준다.
                exit(0)
            #숫자면
            else:
                flag += compare_pop
    elif i ==']':
        flag = 0
        while len(stack)>0:
            compare_pop = stack.pop()
            if compare_pop == '[':
                # 바로 옆에 [ 가 있을 때
                if flag == 0:
                    stack.append(3)
                else:
                    stack.append(3*flag)
                # 짝을 한번 찾으면 break로 while문 빠져나가준다.
                break
            # 잘못된 괄호열
            elif compare_pop == '(':
                print(0)
                # 인자값이 0이 들어가면 종료해준다.
                exit(0)
            #숫자면
            else:
                flag += compare_pop
    
    else:
        stack.append(i)

result = 0
for i in stack:
    # 아직도 괄호가 하나라도 남아 있으면 잘못된 괄호열
    if i == '(' or i == '[':
        print(0)
        # 인자값이 0이 들어가면 종료해준다.
        exit(0)
    else:
        result += i
print(result)