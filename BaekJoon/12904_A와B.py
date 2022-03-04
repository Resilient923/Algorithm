import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

T = list(T)
S = list(S)
while len(T) != len(S):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)

# def dfs(string):
#     # print(string)
#     if len(string) == len(T):
#         if string == T:
#             return 1
#         else:
#             return 0

#     dfs(string[::-1]+'B')
#     dfs(string+'A')

# ans = dfs(S)
# print(ans)