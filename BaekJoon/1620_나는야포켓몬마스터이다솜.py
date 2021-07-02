import sys
input = sys.stdin.readline

# 이문제는 해쉬문제이다.
# 파이썬에서는 딕셔너리로 풀이가능하다.
n,m = map(int,input().split())
data = {}
quiz = []
ans = []
for i in range(n):
    data[str(i+1)] = input().rstrip()
for _ in range(m):
    quiz.append(input().rstrip())

# key에서 value를 가져오는게 아닌 value에서 key를 가져오기위해
# key와 value위치를 바꿨다.
reverse_data = dict(map(reversed,data.items()))

for i in quiz:
    if 48<=ord(i[0])<=57:
        ans.append(data.get(str(i)))
    else:
        ans.append(reverse_data.get(str(i)))
for i in ans:
    print(i)