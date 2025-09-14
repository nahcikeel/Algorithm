def hanoi(n, start, end, temp):
    result = []
    stack = [(n, start, end, temp)]

    while stack:
        n,s,e,t = stack.pop()
        if n == 1:
            result.append((s,e))
        else:
            stack.append((n-1,t,e,s))
            stack.append((1,s,e,t))
            stack.append((n-1,s,t,e))

    return result
    

n = int(input())
result = hanoi(n, 1, 3, 2)
print(len(result))
for s, e in result:
    print(s, e)