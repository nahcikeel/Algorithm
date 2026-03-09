from collections import deque

def bfs(graph, i, n):
    q = deque([i])
    visited = [False] * (n+1)
    visited[i] = True
    
    cnt = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
    return cnt

def solution(n, results):
    
    win_graph  = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    
    for win,lose in results:
        win_graph[win].append(lose)
        lose_graph[lose].append(win)
    
    answer = 0
    for i in range(1, n+1):
        w = bfs(win_graph,  i, n)
        l = bfs(lose_graph, i, n)
        if (w+l) == (n-1):
            answer += 1
    
    return answer