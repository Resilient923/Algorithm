from collections import Counter

str1 = 'FRANCE'
str2 = 'french'

str1_list = []
str2_list = []

cursor1 = 0
while cursor1 < len(str1) - 1:
    temp = ''
    for i in range(cursor1,cursor1+2):
        if 65 <= ord(str1[i]) < 91 or 97 <= ord(str1[i]) < 123:
            temp += str1[i]
    if len(temp) < 2:
        temp = ''
    elif len(temp) == 2:
        str1_list.append(temp)
        temp = ''
    cursor1 += 1

cursor2 = 0
while cursor2 < len(str2) - 1:
    temp = ''
    for i in range(cursor2,cursor2+2):
        if 65 <= ord(str2[i]) < 91 or 97 <= ord(str2[i]) < 123:
            temp += str2[i]
    if len(temp) < 2:
        temp = ''
    elif len(temp) == 2:
        str2_list.append(temp)
        temp = ''
    cursor2 += 1

for i in range(len(str1_list)):
    str1_list[i] = str1_list[i].upper()
for i in range(len(str2_list)):
    str2_list[i] = str2_list[i].upper()

str1_list_cnt = Counter(str1_list)
str2_list_cnt = Counter(str2_list)

intersec = list((str1_list_cnt & str2_list_cnt).elements())
print(intersec)
union = list((str1_list_cnt | str2_list_cnt).elements())
# print('0000000000000000000000')

print(union)
if len(intersec) == 0 and len(union) == 0:
    print(65536)
else:
    print(int(len(intersec)/len(union)*65536))
