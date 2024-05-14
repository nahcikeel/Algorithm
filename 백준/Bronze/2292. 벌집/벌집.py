n = int(input())
cnt = 1
scope = 1

while (n > scope):
    scope += 6*cnt
    cnt += 1

print(cnt)