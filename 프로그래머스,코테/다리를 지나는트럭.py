
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = [0 for _ in range(bridge_length)]
    while truck_weights:
        if sum(bridge[1:]) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            while bridge[1] == 0: # 앞에 0인 값들 한개 빼고 모두 제거 
                bridge.pop(0)
                bridge.append(0)
                cnt +=1
            bridge.append(0)
        cnt+=1
        bridge.pop(0)
    cnt += len(bridge)
    return cnt