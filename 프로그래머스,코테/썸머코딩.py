""" def solution(code, day, data):
    answer = []
    return answer

def parse(word):
    data = []
    for i in range(len(word)):
        if word[i] == "=":
            for j in range(i+1,len(word)):
                data.append(word[j])
    data = ("".join(map(str,data)))
    return data
code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]
data_ = []
for i in range(len(data)):
    data_.append(data[i].split(' '))

ans = [[]for i in range(len(data))]
for i in range(len(data_)):
    for j in data_[i]:
        ans[i].append(parse(j))
num = []
for i in range(len(ans)):
    if ans[i][1] == code:
        if ans[i][2][:8] == day:
            num.append((int(ans[i][0]),int(ans[i][2][8:])))
num = sorted(num,key=lambda x : x[1])
answer = []
for i in num:
    answer.append(i[0])
print(answer) """


t = [0,1,3,0]
r = [0,1,2,3]	
data = []
for i in range(len(t)):
    data.append((t[i],r[i]))
if len(list(set(data)))==len(data):
    data = sorted(data,key=lambda x : x[0])
    ans = []
    for i in data:
        ans.append(i[1])
print(ans)
