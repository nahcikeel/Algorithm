n = int(input())
for _ in range(n):
    r,s = input().split()
    r = int(r)
    result = ''
    for i in s:
        result  += i*r
    print(result)