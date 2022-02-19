import sys

input = sys.stdin.readline

# 소문자로만 이루어져있다.

# 원래 팰린드롬이면 0
# 하나고쳐서  팰린드롬이면 1
# 하나고쳐도 팰린드롬 아니면 2

t = int(input())

def check(word,start,end):
    while start <= end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            return 0
    return 1
    
def solution(word,start,end):
    # 원래 팰린드롬일 때는 뒤집어도 같아야한다.
    if word == word[::-1]:
        return 0
    else:
        # 원래 팰린드롬이 아니라 하나 바꿔야한다면
        # stack은 ababbaba 같은 경우 처리해주기 불편하다.
        while start <= end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            # 두개가 다를 떄 하나 빼고 고려해주는데
            # 왼쪽에서 하나, 오른쪽에서 하나 빼고 되는지 안되는지 본다.
            else:
                left_check = check(word,start+1,end)
                right_check = check(word,start,end-1)
                if left_check or right_check:
                    return 1
                else:
                    return 2


for _ in range(t):
    word = input().rstrip()
    length = len(word)-1
    print(solution(word,0,length))
        

# print(solution("comwwtmoc",0,len("comwwtmoc")-1))
