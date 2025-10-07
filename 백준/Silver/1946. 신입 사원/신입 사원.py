import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = [tuple(map(int, input().split())) for _ in range(n)]


    applicants.sort(key=lambda x: x[0])

    cnt = 1
    min_itv = applicants[0][1]

    for i in range(1,n):
        if applicants[i][1] < min_itv:
            cnt += 1
            min_itv = applicants[i][1]

    print(cnt)