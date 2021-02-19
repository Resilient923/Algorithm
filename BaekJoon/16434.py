import sys
n, h_atk = map(int,sys.stdin.readline().split())
h_hp = 0
cur_hp = 0
h_damage =0
info=[]
for _ in range(n):
    info.append(list(map(int,sys.stdin.readline().split())))



for i in info:
    if i[0] == 1:
        atkcnt = i[2]%h_atk
        if atkcnt == 0 :
            h_damage = -(i[1]*(i[2]//h_atk-1))
        else:
            h_damage = -(i[1]*(i[2]//h_atk))       
    else:
        h_atk += i[1]
        h_damage = i[2]
    cur_hp += h_damage
    if cur_hp>0:
        cur_hp = 0
    h_hp = max(h_hp,abs(cur_hp))
    
print(h_hp+1)
########################################################################
import sys
import math

if __name__ == "__main__":
    # 방의 개수, 초기 공격력
    n, att = map(int, input().split())
    room = []
    for _ in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        room.append(line)

    # 용사의 최소, 최대 hp
    left, right = 1, int(1e18)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        # 용사가 던전에 입장할때 hp, 공격력
        hp, attack = mid, att
        for r in room:
            t, a, h = r[0], r[1], r[2]
            if t == 1:
                hp -= (math.ceil(h / attack) - 1) * a
                if hp <= 0:
                    break
            else:
                attack += a
                hp = min(mid, hp + h)
        if hp > 0:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    print(answer)

