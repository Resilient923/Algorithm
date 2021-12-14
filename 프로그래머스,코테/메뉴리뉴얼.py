from itertools import combinations 
from collections import Counter

# 시간초과는 상관없다
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
answer = []
for i in course:
    temp = []
    for j in orders:
        for k in combinations(j,i):
            temp.append("".join(sorted(k)))
    print(temp)

    ct = Counter(temp).most_common()
    print(ct)

    max_ = 0
    for object in ct:
        if object[1] >= max_:
            # 최대 길이 인것만 추린다.
            max_ = object[1]

    for object in ct:
        if object[1] == max_ and object[1]!=1:
            answer.append(object[0])
print(sorted(answer))
