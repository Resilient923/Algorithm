n = int(input())

words = []
swords =[]
for i in range(n):
    words.append(input())

swords = sorted(words)

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if(len(swords[min_idx])) > len(swords[j]):
            min_idx = j
    swords[i], swords[min_idx] = swords[min_idx], swords[i]


print(swords)
