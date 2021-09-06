
def function(expression,cnt,sign):
    if cnt == 2:
        return str(eval(expression))
    else:
        if sign[cnt] == '*':
            ans = eval('*'.join([function(e,cnt+1,sign) for e in expression.split('*')]))
        elif sign[cnt] == '+':
            ans = eval('+'.join([function(e,cnt+1,sign) for e in expression.split('+')]))
        elif sign[cnt] == '-':
            ans = eval('-'.join([function(e,cnt+1,sign) for e in expression.split('-')]))
    return str(ans)
    

def solution(expression):
    #3개의 연산자가 적용될 수 있는 경우의 수
    signs = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','+','*'],['-','*','+']]
    answer = 0
    for sign in signs:
        ans = abs(int(function(expression,0,sign)))
        answer = max(ans,answer)
    return answer


print(solution("100-200*300-500+20"))