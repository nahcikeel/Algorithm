N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = []

def dfs(start):
    # M개를 모두 골랐다면 출력
    if len(result) == M:
        print(*result)
        return

    # 중복 선택 가능 → 모든 인덱스 탐색
    for i in range(start, N):
        result.append(numbers[i])
        dfs(i)         # i+1이 아니라 0부터 다시 가능
        result.pop()  # 백트래킹

dfs(0)
