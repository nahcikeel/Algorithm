import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

MAX = max(cards)
exist = [0] * (MAX + 1)
score = [0] * (MAX + 1)

# 카드 존재 여부 표시
for c in cards:
    exist[c] = 1

# 약수-배수 관계 계산
for x in cards:
    multiple = x * 2
    while multiple <= MAX:
        if exist[multiple]:
            score[x] += 1
            score[multiple] -= 1
        multiple += x

# 출력 (입력 순서 유지)
print(*[score[c] for c in cards])
