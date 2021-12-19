new_id = "...!@BaT#*..y.abcdefghijklm"	

new_id = new_id.lower()
result = ""

for i in new_id:
    if i.isalnum() or i in '-._':
        result += i
print(result)
while '..' in result:
    result = result.replace('..','.')

if result[0] == '.' and len(result)>1:
    result = result[1:]
if result[-1] == '.':
    result = result[:-1]

if result == '':
    result = 'a'
if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]

if len(result) < 3:
    while len(result) != 3:
        result += result[-1]
    

print(result)