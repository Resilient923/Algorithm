import sys

input = sys.stdin.readline

data = input().rstrip()
bomb_word = input().rstrip()

bomb_length = len(bomb_word)
check_length = bomb_length-1
stack = []

for word in data:
    if bomb_length == 1:
        if word == bomb_word:
            continue
        else:
            stack.append(word)
    else:
        if  len(stack) < check_length:
            stack.append(word)
        else:
            tmp = ''.join(stack[-(check_length):])
            if tmp + word == bomb_word:
                del stack[-(check_length):]
            else:
                stack.append(word)

if stack:
    print(''.join(stack))
else:
    print("FRULA")