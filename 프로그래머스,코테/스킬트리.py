skill = "CBD"
skill_trees = ["BACDE","CBADF","AECB","BDA"]

skill = list(skill)
for i in range(len(skill_trees)):
    skill_trees[i] = list(skill_trees[i])
# 리스트 처리를 해준다    
cnt = 0 

for i in skill_trees:
    match = []
    for j in i:
        if j in skill:
            match.append(j)
    for i in range(len(match)):
        if match[i] != skill[i]:
            break
    else:
        cnt+=1
print(cnt)
            
""" print(skill)
print(skill_trees)
cnt = 0 
flag = []
dp = [True for _ in range(len(skill_trees))]
for i in skill_trees:
    for j in range(len(i)):
        if i[j] == skill[flag]:
            for k in range(0,j):
                if i[k] in skill:
                    dp[skill_trees.index(i)] = False
            flag += 1
print(dp) """    