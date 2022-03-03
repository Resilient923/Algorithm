import sys
input = sys.stdin.readline

data = []
n,m = map(int,input().split())
store = int(input())
for _ in range(store):
    way, coordinate = map(int,input().split())
    data.append((way,coordinate))
d_way, d_coordinate = map(int,input().split())

ans = 0
total = 2 *n + 2*m

for i,j in data:
    if d_way == i:
        # 같은 줄에 있을 때는 그냥 차이 구해서 절댓값 씌우는게 가장 최단거리이다.
        ans += abs(j-d_coordinate)
    # 반대쪽이 아니라 양 옆쪽의 방향에 있을 때
    elif d_way == 1 and i == 4:
        ans += ((n-d_coordinate) + j)
    elif d_way == 1 and i == 3:
        ans += (d_coordinate + j)
    elif d_way == 2 and i == 3:
        ans += (d_coordinate + (m-j))
    elif d_way == 2 and i == 4:
        ans += ((n-d_coordinate) + (m-j))
    elif d_way == 3 and i == 1:
        ans += (d_coordinate+j)
    elif d_way == 3 and i == 2:
        ans += ((m-d_coordinate) + j)
    elif d_way == 4 and i == 1:
        ans += (d_coordinate + (m-j))
    elif d_way == 4 and i == 2:
        ans += ((m-d_coordinate) + (n-j))

    # 반대에 있을 때
    elif d_way == 1 and i == 2:
        if d_coordinate + m + j <= total // 2:
            ans += d_coordinate + m +j
        else:
            ans += (n-d_coordinate) + m + (n-j)
    elif d_way == 2 and i == 1:
        if d_coordinate + m + j <= total // 2:
            ans += d_coordinate + m +j
        else:
            ans += (n-d_coordinate) + m + (n-j)
    elif d_way == 3 and i == 4:
        if d_coordinate + n + j <= total // 2:
            ans += d_coordinate + n +j
        else:
            ans += (m-d_coordinate) + n + (m-j)
    elif d_way == 4 and i == 3:
        if d_coordinate + n + j <= total // 2:
            ans += d_coordinate + n +j
        else:
            ans += (m-d_coordinate) + n + (m-j)

print(ans)