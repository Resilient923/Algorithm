
def solution(clothes):
    answer = 1
    data = {}
    for i in clothes:
        if i[1] in data:
            data[i[1]] += 1
        else:
            data[i[1]] = 1
    
    for i in data.values():
        # 입거나 안입거나 니까
        # 안입을경우를 1씩 더해서 곱해준다.
        answer *= (i+1)
    # 근데 모두 안입는경우는 안되니까 1을 빼준다.
    return answer -1 

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))