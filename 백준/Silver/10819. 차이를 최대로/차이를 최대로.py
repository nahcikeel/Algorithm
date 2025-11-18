n = int(input())
arr = list(map(int, input().split()))

used = [False] * n
result = 0
perm = []

def calc(v):
    s = 0
    for i in range(len(v)-1):
        s += abs(v[i] - v[i+1])
    return s

def dfs():
    global result
    
    if len(perm) == n:
        result = max(result, calc(perm))
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            perm.append(arr[i])
            dfs()
            perm.pop()
            used[i] = False

dfs()
print(result)
