# 9012

n = int(input())

for _ in range(n):
    vps = input()
    stack = []

    for i in vps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')