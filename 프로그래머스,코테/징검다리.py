def solution(distance, rocks, n):
    answer = 0
    # rocks를 오름차순으로 정렬해서 0에서 가까운 거리 순서대로 바위들을 위치시켜준다.
    rocks.sort()
    # 이분탐색을 위한 start, end설정
    start = 0
    end = 1000000000
    # 이분탐색을 위해 while문 조건을 만들어준다.
    while start <= end:
        mid = (start+end)//2
        # 현재 기준이 되는 바위 위치 저장해두는 변수
        current_rock = 0
        # 제거한 바위의 개수 0으로 초기화
        remove_rock = 0
        # 각 mid값에서 최솟값을 갱신해줄 Min 변수 생성
        Min = 1000000000
        # 정렬한 rocks를 순서대로 돌면서
        for rock in rocks:
            # 현재 mid값과 비교하기위한 값
            # 바위 위치에서 현재 비교중인 바위까지의 차이를 diff에 저장
            diff = rock - current_rock
            # diff가 mid 보다 작으면 바위 제거하고 카운트 1올려준다.
            if diff < mid:
                remove_rock += 1
            # diff가 mid랑 같거나 크면
            else:
                # 현재 rock 바위위치를 현재 비교중인 바위위치 갱신
                current_rock = rock
                # 해당 mid 단계에서의 최소거리인지 체크
                Min = min(Min,diff)
        # 제거한 바위개수가 n보다 크면 mid값을 줄여줘야하기 때문에 end = mid-1
        # 바위를 너무 많이 제거 했다. mid를 줄여서 바위를 조금만 제거하자
        if remove_rock > n:
            end = mid - 1
        # 제거한 바위개수가 n하고 같거나 작으면 mid값을 늘려줘야 하기 때문에 Start = mid+1해준다.
        else:
            # 최솟값 중에 가장 큰 값을 return해야 하므로 마지막 mid값이 정해질 때 Min값을 return 해준다.
            # mid를 늘려서 바위를 더 제거하거나 mid의 최댓값을 올려보자
            answer = Min
            start = mid + 1
    
    return answer