
sticker = [14]

def solution(sticker):
    answer = 0
    if len(sticker)==1:
        answer = sticker[0]
    else:
        dp1 = [0]*(len(sticker)+2)
        dp1[0] = sticker[0]
        dp1[1] = sticker[0]
        for i in range(2,len(sticker)-1):
            dp1[i] = max(dp1[i-1],dp1[i-2]+sticker[i])

        dp2 = [0]*(len(sticker)+2)
        dp2[0] = 0
        dp2[1] = sticker[1]
        for i in range(2,len(sticker)):
            dp2[i] = max(dp2[i-1],dp2[i-2]+sticker[i])
    
    answer = max(max(dp1),max(dp2))

    return answer

print(solution(sticker))