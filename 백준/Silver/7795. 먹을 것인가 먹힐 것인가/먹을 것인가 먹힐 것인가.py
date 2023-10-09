import sys

N = int(input())

for _ in range(N):    # 반복횟수 인풋
    
    s,t = map(int, sys.stdin.readline().split())     
    a = list(map(int, sys.stdin.readline().split()))    
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()
    b.sort()

    cnt = 0
    ans = 0

    for i in range(s):    # b의 길이만큼 반복
        while True:
             if cnt == t or a[i] <= b[cnt]:    # a의 원소가 b의 원소보다 작아지거나, t의 원소를 다 돌면
                ans += cnt    # answer에 cnt 더해주면서 탈출
                break
             else:
                cnt += 1    # 아니라면 +1씩 증가
       
    print(ans)

