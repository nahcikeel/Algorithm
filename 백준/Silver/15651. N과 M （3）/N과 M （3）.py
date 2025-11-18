n, m = map(int, input().split())
res = []

def dfs(depth):
    if depth == m:
        print(*res)
        return
    
    for i in range(1, n+1):
        res.append(i)
        dfs(depth+1)
        res.pop()

dfs(0)
