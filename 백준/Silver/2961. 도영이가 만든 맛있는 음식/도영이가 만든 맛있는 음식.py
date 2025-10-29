import sys
input = sys.stdin.readline

N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')

def dfs(idx, sour, bitter, used):
    global min_diff
    if idx == N:
        if used:
            diff = abs(sour - bitter)
            min_diff = min(min_diff, diff)
        return

    s, b = ingredients[idx]
    dfs(idx + 1, sour * s, bitter + b, True)
    dfs(idx + 1, sour, bitter, used)

dfs(0, 1, 0, False)
print(min_diff)
