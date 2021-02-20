#1439
s = list(input())
onecnt = 0
zerocnt =0
cnt =0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        if s[i-1]=='0':
            onecnt+=1
        else:
            zerocnt+=1
if s[-1]=='0':
    onecnt+=1
else:
    zerocnt+=1


print(min(zerocnt,onecnt))
