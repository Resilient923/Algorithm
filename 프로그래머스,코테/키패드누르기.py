def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
#거리구하는 함수
def solution(numbers, hand):

    answer = ''
    keypad = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    left = '*'
    right = '#'
    
  
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            left = i
        elif i in [3,6,9]:
            answer+='R'
            right = i
        elif i in [2,5,8,0]:
            if distance(keypad[left],keypad[i]) < distance(keypad[right],keypad[i]):
                answer+='L'
                left = i
            elif distance(keypad[right],keypad[i]) < distance(keypad[left],keypad[i]):
                answer+='R'
                right = i
            else:
                if hand == "right":
                    answer+='R'
                    right = i
                else:
                    answer+='L'
                    left = i
    return answer