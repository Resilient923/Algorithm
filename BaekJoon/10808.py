graph = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in graph: 
    dic[i] = 0
for j in input(): 
    dic[j] += 1
print(' '.join(map(str, dic.values())))