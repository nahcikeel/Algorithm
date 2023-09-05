n = int(input())

ki = []                        # 작업을 수행할 리스트
chan = []                      # 정답을 담을 리스트

for i in range(1,n+1):         # 1부터 n까지를 ki에 삽입
    ki.append(i)

while len(ki) > 0:             # 작업리스트에 원소가 있다면 계속 진행
    chan.append(ki.pop(0))     # 맨앞 원소를 정답리스트에 추가
    if len(ki) > 0:            # 다음 원소는 작업리스트에 추가
        ki.append(ki.pop(0))   # if 조건이 없다면 한번에 두가지를 수행하지 못함. => 맨앞원소 제거 + 다음원소 추가

for j in chan:                 # 문자열로 출력
    print(j, end=" ")
