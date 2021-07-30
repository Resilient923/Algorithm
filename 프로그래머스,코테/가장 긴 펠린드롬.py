def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            List = s[i:j]
            if List == List[::-1]:
                answer = max(answer,len(s[i:j]))
    return answer
print(solution("abaabaaaaaaa"))

# "abba" = 4
# "abaabaaaaaaa" = 7









# from collections import deque

# def solution(s):
#     answer = 0
#     temp = []
#     flag = 0
#     for i in s:
#         if i in temp:
#             if flag == 0:
#                  temp.pop()
#             alphabet = temp.pop()
#             if alphabet == i :
#                 answer += 2
#                 flag = 1
#         else:
#             temp.append(i)

#     return answer + 1