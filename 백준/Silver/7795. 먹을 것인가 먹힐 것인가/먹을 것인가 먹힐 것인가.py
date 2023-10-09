import sys

N = int(input())

for _ in range(N):
    
    s,t = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    cnt = 0

    a.sort()
    b.sort()

    cnt = 0
    ans = 0

    for i in range(s):
        while True:
             if cnt == t or a[i] <= b[cnt]:
                ans += cnt
                break
             else:
                cnt += 1
       
    print(ans)

