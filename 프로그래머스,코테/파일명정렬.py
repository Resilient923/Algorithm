def solution(files):
    answer = []
    # 파일 하나를 리스트로 만들고, HEAD 따로, NUMBER는 string으로 받아서 Int로 바꾸고
    # TAIL 이렇게 넣어준다.
    
    # 파싱한 값들을 순서대로 넣어줄 리스트 생성
    fileList = [[] for _ in range(len(files))]
    for i in range(len(files)):
        data = files[i]
        tmp = 0
        fileList[i].append(i)
        for j in range(len(data)):
            # 아스키 코드가 숫자일때,
            if 48<=ord(data[j])<=57:
                # 대소문자 차이없으니까 대문자로 다 바꾼다.
                fileList[i].append(data[:j].upper())
                tmp = j
                break
        # NUMBER 파싱한 값들
        tmp_number = ''
        
        # bar020 같은 경우를 잡아내야한다.
        print(tmp)
        number = tmp
        while 48<=ord(data[number])<=57 and number < len(data)-1:
            tmp_number += data[number]
            number += 1
            
        fileList[i].append(int(tmp_number))
        # TAIL 파싱한 값들
        if number < len(data):
            fileList[i].append(data[number:])
        print(tmp_number)
        # print(data[number:])

        
    # HEAD정렬하고 NUMBER정렬
    fileList.sort(key=lambda x:(x[1],x[2]))
    
    # print(fileList)
    # 인덱스 순서대로 answer에 넣어준다.
    for file in fileList:
        answer.append(files[file[0]])
        
    return answer


print(solution(["MUZI010", "muzi1.png"]))