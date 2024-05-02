n = str(input())

result = 0
answer = -1

if '0' not in n:
    print(answer)

else:
    for i in range(len(n)):
        result += int(n[i])
    
    if result%3 != 0:
        print(answer)
    else:
        answer = sorted(n,reverse=True)
        print(''.join(answer))