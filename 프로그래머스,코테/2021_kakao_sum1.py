
s = "one4seveneight" 
""" "23four5six7"
"2three45sixseven"
"123" """
def word(list):
    a = ''.join(list)
    return a

def solution(s):
    temp = []
    answer= []
    for i in s:
        if 122>=ord(i)>=97:
            temp.append(i)
            if word(temp) == 'zero':
                answer.append(0)
                temp = []
            elif word(temp) == 'one':
                answer.append(1)
                temp = []
            elif word(temp) == 'two':
                answer.append(2)
                temp = []
            elif word(temp) == 'three':
                answer.append(3)
                temp = []
            elif word(temp) == 'four':
                answer.append(4)
                temp = []
            elif word(temp) == 'five':
                answer.append(5)
                temp = []
            elif word(temp) == 'six':
                answer.append(6)
                temp = []
            elif word(temp) == 'seven':
                answer.append(7)
                temp = []
            elif word(temp) == 'eight':
                answer.append(8)
                temp = []
            elif word(temp) == 'nine':
                answer.append(9)
                temp = []
        elif 57>=ord(i)>=48:
            answer.append(int(i))
    
    answer = ("".join(map(str,answer)))
    

    return int(answer)


