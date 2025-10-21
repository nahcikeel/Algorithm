import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]

    i = j = cnt = 0
    while i < n and j < m:
        if a[i] == b[j]:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(cnt)
