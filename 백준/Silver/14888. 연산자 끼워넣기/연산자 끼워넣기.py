import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, divis = map(int, input().split())

max_num = -int(1e9)
min_num = int(1e9)

def dfs(idx, num, plus, minus, multi, divis):
    global max_num, min_num

    if idx==n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    if plus>0:
        dfs(idx+1, num+nums[idx], plus-1, minus, multi, divis)

    if minus>0:
        dfs(idx+1, num-nums[idx], plus, minus-1, multi, divis)
    
    if multi>0:
        dfs(idx+1, num*nums[idx], plus, minus, multi-1, divis)
    
    if divis>0:
        if num < 0:
            dfs(idx+1, -(-num // nums[idx]), plus, minus, multi, divis-1)
        else:
            dfs(idx+1, num // nums[idx], plus, minus, multi, divis-1)

dfs(1,nums[0],plus, minus, multi, divis)

print(max_num)
print(min_num)