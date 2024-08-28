import sys
input = sys.stdin.readline

n,m = map(int, input().split())

participants = [i for i in range(1,n+1)]    # 파티에 참가하는 전체 참가자
party = [0]*m   # 파티의 개수

t = input()

if t == '0':
    t_people = []

else:
    t = list(map(int, t.split()))
    t_people = t[1:]

for k in range(m):
    party[k] = list(map(int, input().split()))[1:]

for _ in range(m):
    for sub in party:
        if any(item in sub for item in t_people):
            for item in sub:
                if item not in t_people:
                    t_people.append(item)

answer = 0
for sub in party:
    if not any(item in sub for item in t_people):
        answer += 1

print(answer)