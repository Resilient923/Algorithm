""" def solution(dirs):
    answer = 0
    x,y = 5,5
    already = [(5,5)]
    for i in dirs:
        if i == "U":
            x = x - 1
        elif i == "D":
            x = x + 1
        elif i == "R":
            y = y + 1
        elif i == "L":
            y = y - 1
        if x>=0 and x<=10 and y>=0 and y<=10:
            already.append((x,y)
    answer += len(list(set(already)))
    return answer """
def solution(dirs):
    already = set()
    start =(5,5)
    for i in dirs:
        x,y = start
        if i == "U":
            x = x - 1
        elif i == "D":
            x = x + 1
        elif i == "R":
            y = y + 1
        elif i == "L":
            y = y - 1
        if x>=0 and x<=10 and y>=0 and y<=10:
            nextdot = x,y
            already.add((nextdot,start))
            already.add((start,nextdot))
            start = nextdot
    return len(already) // 2
