def solution(n, words):
    temp =[]
    temp.append(words[0])
    ans =[]
    for i in range(1,len(words)):
        if words[i] in temp or words[i-1][-1] != words[i][0]:
            #print(words.index(words[i]))
            if (i+1)%n==0:
                ans.append(n)
            else:
                ans.append((i+1)%n)
            turn = (i+1)/n
            if int(turn) != turn: #이부분 수정
                turn = int(turn) + 1

            ans.append(turn)
            break
        temp.append(words[i])
    if len(ans) == 0:
        ans.append(0)
        ans.append(0)
    

    return ans
n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
""" n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"] """
""" n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"] """
#result = [words[i * n:(i + 1) * n] for i in range((len(words) + n - 1) // n )] 

print(solution(n,words))

  