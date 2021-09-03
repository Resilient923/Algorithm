# def solution(gems):
    
#     # length = len(gems)
#     set_gems = set(gems)
#     length = len(set_gems)
#     if length == 1:
#         return [1,1]
#     # print(length)
#     # print(len(gems))
#     result = []
#     for i in range(len(gems)-length):
#         answer = []
#         temp = []
#         answer.append(i+1)
#         temp.append(gems[i])
#         for j in range(i+1,i+1+length):
#             temp.append(gems[j])
#             if set(temp) == set_gems:
#                 # print(answer)
#                 answer.append(j+1)
#                 result.append([i+1,j+1])
#                 break
#     result.sort(key=lambda x:x[0])
#     # print(result)
#     Min = result[0][1] - result[0][0]
#     ans = result[0]
#     for i in result:
#         if i[1]-i[0] < Min:
#             Min = i[1]-i[0]
#             ans = i
#     return ans
def solution(gems):
    length = len(set(gems)) 
    gem_length = len(gems)
    start = 0 
    end = 0
    temp = [0, gem_length]
    dic = {gems[0] : 1}
    while start < gem_length and end < gem_length:
        print(dic)
        if len(dic) == length:
            if end-start < temp[1] -temp[0]:
                temp = [start, end]

            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == gem_length:
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [temp[0]+1,temp[1]+1]

gems = ["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]
#  ["A","A","A","B","B"][3,4]
#  ["A"] [1,1]
#  ["A","B","B","B","B","B","B","C","B","A"][8,10]
#  ["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"][3, 7]
print(solution(gems))
