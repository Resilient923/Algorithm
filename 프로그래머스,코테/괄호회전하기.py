from collections import deque
# 올바른 괄호 문자열일때
def check(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if not stack:
                return False
            x = stack.pop()
            if c == ')' and x != '(':
                return False
            elif c == ')' and x != '(':
                return False
            elif c == '}' and x != '{':
                return False
    if len(stack) == 0:
        return True

def solution(s):
    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        # 왼쪽으로 한칸씩 이동
        s.rotate(-1)
        if check(s):
            answer += 1
    return answer
