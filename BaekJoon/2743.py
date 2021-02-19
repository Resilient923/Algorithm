n = list(input())
for i in range(len(n)):
    if n[i].isupper():
        if ord(n[i])+13 <= 90:
            n[i] = chr(ord(n[i])+13)
        else:
            n[i] = chr(ord(n[i])-13)
    elif n[i].islower():
        if ord(n[i])+13 <= 122:
            n[i] = chr(ord(n[i])+13)
        else:
            n[i] = chr(ord(n[i])-13)

for i in n:
    print(i, end="")

