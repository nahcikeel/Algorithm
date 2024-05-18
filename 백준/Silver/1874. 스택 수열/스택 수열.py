n = int(input())
stack = []
result = []
cnt = 1

for _ in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    
if len(stack) == 0:
    for i in result:
        print(i)
else:
    print('NO')