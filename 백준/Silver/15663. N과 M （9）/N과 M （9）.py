n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

visited = [False] * n
result = []

def dfs(path):
    if len(path) == m:
        print(*path)
        return
    
    used_in_this_level = set()
    
    for i in range(n):
        if not visited[i] and nums[i] not in used_in_this_level:
            visited[i] = True
            used_in_this_level.add(nums[i])
            dfs(path + [nums[i]])
            visited[i] = False

dfs([])