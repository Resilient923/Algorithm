def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    print(s)
    s.sort(key=len)
    print(s)
    for i in s:
        data = i.split(',')
        print('data:',data)
        for j in data:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


s = "{{20,111},{111}}"

print(solution(s))