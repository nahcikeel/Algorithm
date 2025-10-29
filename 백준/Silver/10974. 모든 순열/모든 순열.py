N = int(input())

visited = [False] * (N + 1)
result = []

def dfs():
    if len(result) == N:
        print(*result)
        return

    for i in range(1, N + 1):
        if not visited[i]:      
            visited[i] = True   
            result.append(i)

            dfs()                

            visited[i] = False
            result.pop()

dfs()
