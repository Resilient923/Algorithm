from collections import defaultdict

def solution(record):
    answer = []
    tmp = []
    # 채팅 방 닉네임 변경 1. 나간 후 다시 들어오기 2. 현재 채팅방에서 변경 -> 전체가 다 바뀜
    # 길이 10만
    # 딕셔너리
    dict = defaultdict(str)
    for i in range(len(record)):
        word = record[i].split(' ')
        order = word[0]
        if order == "Enter":
            dict[word[1]] = word[2]
            tmp.append((("e",word[1])))
        elif order =='Leave':
            tmp.append(("l",word[1]))
        elif order == "Change":
            dict[word[1]] = word[2]
    for a,b in tmp:
        if a == 'e':
            answer.append(dict[b]+"님이 들어왔습니다.")
        elif a == 'l':
            answer.append(dict[b]+"님이 나갔습니다.")
    # Muzi 님이 들어왔습니다 -> Prodo
    # Prodo 님이 들어왔습니다 -> Ryan
    # Muzi 님이 나갔습니다 -> Prodo
    # Prodo 님이 들어왔습니다
    return answer