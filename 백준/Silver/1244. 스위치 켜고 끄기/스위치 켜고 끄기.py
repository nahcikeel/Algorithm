n = int(input())
switches = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    s, number = map(int, input().split())

    if s == 1:
        for i in range(n):
            if (i+1) % number == 0:
                switches[i] = 1 if switches[i] == 0 else 0

    else:
        idx = number - 1
        left = idx
        right = idx

        while left >= 0 and right < n and switches[left] == switches[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1

        for i in range(left, right + 1):
            switches[i] = 1 if switches[i] == 0 else 0

for i in range(n):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
