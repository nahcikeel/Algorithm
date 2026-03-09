from collections import deque

def solution(n, roads, sources, destination):

    
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    dist = [-1] * (n+1)
    q = deque([destination])
    dist[destination] = 0
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    answer = []
    for s in sources:
        answer.append(dist[s])
    
    return answer