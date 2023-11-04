# n횟수 인풋받기
n = int(input())

for i in range(n):

    ox = list(input())
    cnt = 0
    sum_cnt = 0

    for j in ox:
        if j == 'O':
            cnt += 1
            sum_cnt += cnt
        else:
            cnt = 0
    print(sum_cnt)
