# notSelf : 생성자 있는 숫자

ALL = list(range(1,10001))  # 전체 1~10000 
notSelf = []

for i in range(1,10001):
    for j in str(i):    
        i += int(j)        # 전체숫자+자릿수 더해주기
    if i <= 10000:
            notSelf.append(i)    # 10000이하면 리스트에 추가

notSelf = list(set(notSelf))     # set으로 중복 제거하고 다시 set에 넣기 

for m in notSelf:
    if m in ALL:
        ALL.remove(m)  # 1~10000 중에 겹치는 숫자 제거

for n in ALL:
    print(n)
