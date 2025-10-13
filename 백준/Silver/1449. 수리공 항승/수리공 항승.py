n, l = map(int, input().split())
leaks = list(map(int, input().split()))
leaks.sort()

count = 0
i = 0

while i < n:
    start = leaks[i]         # 새 테이프 시작 위치
    end = start + l - 1      # 테이프로 덮이는 마지막 위치
    count += 1

    # 테이프로 덮이는 위치 스킵
    while i < n and leaks[i] <= end:
        i += 1

print(count)
