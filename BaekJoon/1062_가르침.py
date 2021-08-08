# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n,k = map(int,input().split())

# first_word = {'a','n','t','i','c'}


# # a,n,t,i,c 를제외한 알파벳들 리스트
# remain_word = set(chr(i) for i in range(97, 123)) - first_word
# data = [set(input().rstrip()[4:-4])-first_word for _ in range(n)]

# result = 0
# # 5보다 작으면 anta, tica를 만들수 없으므로 0개
# if k < 5:
#     print(0)
# else:
#     for i in list(combinations(remain_word,k-5)):
#         ans = 0
#         for data in data:
#             if not set(words) - set(i):
#                 ans += 1
#         if result < ans:
#             result = ans
#     print(result)
from itertools import combinations 
import sys
n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함

first_word = {'a','n','t','i','c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word
data = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

def countReadableWords(data, learned):
   cnt = 0
   for word in data:
      canRead = 1
      for w in word:
          # 안배웠으니까 못읽는다.
         if learned[ord(w)] == 0:
            canRead = 0
            break
      if canRead == 1:
         cnt += 1
   return cnt

if k >= 5:
   learned = [0] * 123
   for x in first_word:
      learned[ord(x)] = 1

   # 남은 알파벳 중에서 k-5개를 선택해본다.
   for teach in list(combinations(remain_alphabet, k-5)):
      for t in teach:
         learned[ord(t)] = 1
      cnt = countReadableWords(data, learned)

      if cnt > answer:
         answer = cnt
      for t in teach:
         learned[ord(t)] = 0
   print(answer)
else:
   print(0)


