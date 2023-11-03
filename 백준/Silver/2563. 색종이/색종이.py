paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    h,w = map(int, input().split())

    for x in range(h,h+10):
        for y in range(w,w+10):
            paper[x][y] = 1

cnt = 0

for i in paper:
    cnt += i.count(1)

print(cnt)