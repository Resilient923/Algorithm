def divide(w):
    open_cnt = 0
    close_cnt = 0
    for i in range(len(w)):
        if w[i] == "(":
            open_cnt += 1
        else:
            close_cnt += 1
        if open_cnt == close_cnt:
            return w[:i+1], w[i+1:]

def perfectString(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p: #1
        return ""
    
    u,v = divide(p) #2
    
    if perfectString(u): #3
        return u + solution(v)
    
    else: #4
        tmp = "(" # 4-1
        tmp += solution(v) # 4-2
        tmp += ")" # 4-3
        
        for i in u[1:len(u)-1]: # 4-4
            if i == '(':
                tmp += ')'
            else:
                tmp += '('
                
    return tmp