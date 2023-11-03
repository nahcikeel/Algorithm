paper = [[0 for _ in range(100)] for _ in range(100)]  # 2차원 배열 (도화지) 생성

n = int(input())  # 장수 입력

for _ in range(n):
    h,w = map(int, input().split())  # 색종이 입력

    for x in range(h,h+10):
        for y in range(w,w+10):
            paper[x][y] = 1    # 색종이로 덮인 부분은 1로 배열 채우기

cnt = 0

for i in paper:
    cnt += i.count(1)    # 배열에서 1만 세기

print(cnt)
