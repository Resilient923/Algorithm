import sys
input = sys.stdin.readline
def function(n):
    number = 0
    cnt = 0
    while True:
        number +=1 
        movie_name = str(number)
        if movie_name.count("666") > 0:
            title = number
            cnt += 1
        if cnt == n:
            break
    return title

n = int(input())
print(function(n))
