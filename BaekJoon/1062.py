import sys
input = sys.stdin.readline

n,k = map(int,input().split())

words = []
word= []
first_word = ['a','n','t','i','c']
for i in range(n):
    words.append(input())
for i in words:
    for j in i:
        word.append(j)
print(set(word))
