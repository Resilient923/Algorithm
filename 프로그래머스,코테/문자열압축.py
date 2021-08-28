def solution(s):
    answer = []
    result = ''
    if len(s) == 1:
        return 1
    for i in range(1,len(s)):
        cnt = 1
        temp = s[:i]
        for j in range(i,len(s),i):
            if s[j:j+i] == temp:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ''
        result += str(cnt) + temp
        answer.append(len(result))
        result = ''


    return min(answer)

s = "abcabcabcabcdededededede"

print(solution(s))