t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    d = y-x

    if d == 0:
        print(0)
        continue

    cnt = 1
    s = 1
    last = 1

    while s < d:
        rem = d-s
        cur = last

        # 속도 높인 버전 검사
        if rem >= (cur + 1) * ((cur + 1)+1)//2 : 
            last = (cur + 1)

        # 속도 유지 버전 검사
        elif rem >= cur * (cur+1)//2:
            last = cur
        
        # 속도 감소 버전 검사
        else:
            last = max(1, cur-1)

        s += last
        cnt += 1

    print(cnt)
