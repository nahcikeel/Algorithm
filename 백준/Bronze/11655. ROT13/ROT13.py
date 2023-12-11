# ord('a') : 97
# ord('z') : 122
# ord('A') : 65
# ord('Z') : 90


secret = input()
answer = ''

for i in secret:
    
    if ord(i) >= 97 and ord(i) <= 109:
        answer +=(chr(ord(i)+13))
    elif ord(i) >= 110 and ord(i) <= 122:
        answer+=(chr(ord(i)-13))
    elif ord(i) >= 65 and ord(i) <= 77:
        answer+=(chr(ord(i)+13))
    elif ord(i) >= 78 and ord(i) <= 90:
        answer+=(chr(ord(i)-13))
    else:
        answer+=(i)

print(answer)