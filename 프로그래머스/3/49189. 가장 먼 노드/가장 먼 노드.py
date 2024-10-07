from collections import deque

def solution(n, edge):
    
    visited = [-1 for _ in range(n+1)]
    
    graph = [[]for _ in range(n+1)]
    for start,end in edge:
        graph[start].append(end)
        graph[end].append(start)
        
    q = deque()
    q.append(1)
    
    visited[1] = 1
    
    while q:
        current_node = q.popleft()
        
        for neighbor in graph[current_node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current_node]+1
                q.append(neighbor)
    
    max_num = max(visited)
    answer = sum(1 for i in visited if i == max_num)
        
        
    return answer