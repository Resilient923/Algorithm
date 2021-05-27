def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        a = (timetable[i].split(":"))
        # 시간을 분으로 환산
        timetable[i]=int((int(a[0])*60+int(a[1])))
    timetable.sort()
    # 가장 늦은시간을 구해야하므로 final_time에서 조금식 빼주는 형태로 간다.
    final_time = 60*9+(n-1)*t
    

    for i in range(n):
        if len(timetable)<m:
            return ("%02d:%02d" %(final_time//60,final_time%60))
        #맨 마지막 셔틀버스 운행할때
        if i == n-1:   
            # 가장 대기열에 빨리 도착하는 크루가, 마지막출발시간 보다 작으면 일단 크루 한명은 무조건타는거니까 재껴두고
            # 남아있는 timetable에서 m명안에 들기위해서 m번째 사람보다 1분 빨리오면 된다.
            if timetable[0]<=final_time:
                final_time = timetable[m-1]-1
            return ("%02d:%02d" %(final_time//60,final_time%60))
        for j in range(m-1,-1,-1):
            # 정렬해놨으니까 맨뒤에 크루부터 for문 돌리면서 출발시간보다 작으면 먼저 태워보낸다.
            # 콘은 맨 마지막 버스에만 타면 된다.
            # 마지막 버스 하나만 남겨놓고 다 태운다.
            start_time = (60*9) + i*t
            if timetable[j]<=start_time:
                del timetable[j]

timetable = ["09:10", "09:09", "08:00"]
n = 2
t = 10
m = 2

print(solution(n,t,m,timetable))



