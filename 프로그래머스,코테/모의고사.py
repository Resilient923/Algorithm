answers = [1,3,2,4,2]
ans = []
students = []
students.append([1,2,3,4,5]*2000)
students.append([2,1,2,3,2,4,2,5]*1250)
students.append([3,3,1,1,2,2,4,4,5,5]*1000)

cnt = [0]*len(answers)

for i in range(3):
    for j in range(len(answers)):
        if students[i][j] == answers[j]:
            cnt[i] +=1

cnt.sort(reverse=True)

answer = []
for i in range(3):
    if cnt[i] == max(cnt):
        answer.append(i+1)
print(answer)