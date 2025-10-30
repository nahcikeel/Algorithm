N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = []

def dfs(start):
    # M개를 모두 골랐으면 출력
    if len(result) == M:
        print(*result)
        return

    # start 인덱스부터 N까지 반복
    for i in range(start, N):
        result.append(numbers[i])
        dfs(i + 1)  # i 이후부터만 선택 (오름차순 유지)
        result.pop()  # 백트래킹

dfs(0)
