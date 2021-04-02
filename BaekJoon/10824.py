import sys
input = sys.stdin.readline

data = list(map(int,input().split()))



def cnt(num):
    return len(str(num))

ans = (data[0]*(10**cnt(data[1]))+data[1])+(data[2]*(10**cnt(data[3]))+data[3])

print(ans)
