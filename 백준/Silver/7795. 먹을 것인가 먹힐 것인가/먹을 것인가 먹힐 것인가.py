import sys

N = int(input())

for _ in range(N):    # 반복횟수 인풋
    
    s,t = map(int, sys.stdin.readline().split())     
    a = list(map(int, sys.stdin.readline().split()))    
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()
    b.sort()

    cnt = 0    # 'a의 원소 > b의 원소' 개수를 셀 변수
    ans = 0    # 누적된 정답을 담을 변수

    for i in range(s):    # a의 길이만큼 반복
        while True:
             if cnt == t or a[i] <= b[cnt]:    # t의 원소를 다 돌거나(a의 원소가 모두 b의 원소보다 크면), a의 원소가 b의 원소보다 작아지면
                ans += cnt    # ans에 cnt 더해주면서 종료 => 다음 a원소 시작
                break
             else:
                cnt += 1    # 아니라면 +1씩 증가(a의 원소 > b의 원소)  
       
    print(ans)

