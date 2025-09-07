import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(idx, total, plus, minus, multiply, divide):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    if plus > 0:
        dfs(idx+1, total + nums[idx], plus-1, minus, multiply, divide)

    if minus > 0:
        dfs(idx+1, total - nums[idx], plus, minus-1, multiply, divide)

    if multiply > 0:
        dfs(idx+1, total * nums[idx], plus, minus, multiply-1, divide)

    if divide > 0:
        if total < 0:
            dfs(idx+1, -(-total // nums[idx]), plus, minus, multiply, divide-1)
        else:
            dfs(idx+1, total // nums[idx], plus, minus, multiply, divide-1)

dfs(1, nums[0], plus, minus, multiply, divide)

print(max_val)
print(min_val)
