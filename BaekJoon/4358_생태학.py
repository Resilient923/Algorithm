from collections import defaultdict
import sys

input = sys.stdin.readline
dict = defaultdict(int)

word_cnt = 0
while 1:
        word = input().rstrip()
        if not word:
            break
        dict[word] += 1
        word_cnt += 1
    # except EOFError:
    #     break
    
# print(dict)
dict_list= list(dict.keys())
dict_list.sort()

for d in dict_list:
    print('%s %.4f' %(d,dict[d]/ word_cnt * 100))
# round(cnt,4)