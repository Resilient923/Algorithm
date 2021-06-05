from itertools import combinations,permutations
import sys
input = sys.stdin.readline

while True:
    num = list(map(int,input().split()))
    if num[0] == 0:
        break
    num.pop(0)
    a = list(combinations(num,6))
    for i in a:
        for j in range(len(i)):
            print(i[j],end=" ")
        print("")
    print("")

