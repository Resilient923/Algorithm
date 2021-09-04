def solution(n,stages):
    Counter = {}
    # n이 COunter에 없을 경우를 고려해주기 위해
    # 일단 n까지의 key 값에 value를 0으로 초기화해준다.
    for i in range(n):
        Counter[i+1] = 0
    # 여기서 stages리스트에 주어진 값으로 Counter 딕셔너리를 갱신해준다.
    for i in stages:
        if i <=n:
            if i not in Counter:
                Counter[i] = 0
            Counter[i] += 1
    # 실패율을 구해주기 위한 총 인원수
    user = len(stages)
    # 실패율을 담을 딕셔너리
    fail_percentage = {}
    for i in Counter.keys():
        # 스테이지는 n개이고 n+1(모든스테이지통과했을경우)를 고려해준다.
        if i <=n:
            # 이부분 중요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # Counter값이 0일경우 0을 나눌수가 없으므로 인덱스 에러가 발생할 수 있다.
            if Counter[i] == 0:
                fail_percentage[i] = 0
            else:
                fail_percentage[i] = Counter[i]/user
            # 나중에 for문으로 자기보다 낮은 스테이지를 통과한 인원수는
            # 제외시킨다.
            user -= Counter[i]
    # value값(실패율) 을 기준으로 내림차순 정렬해주고 
    fail_percentage = dict(sorted(fail_percentage.items(),key = lambda x: x[1],reverse=True))
    # 리스트형식으로 정렬된 데이터의 key값만 출력하면된다.
    answer = list(fail_percentage.keys())
    return answer


stages = [4,4,4,4,4]
n = 4
print(solution(n,stages))