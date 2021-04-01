import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    number, words = input().split()
    alp = []
    ans = []
    for i in list(words):
        alp.append(i)
    for i in alp:
        for j in range(int(number)):
            ans.append(i)
    print("".join(ans))
