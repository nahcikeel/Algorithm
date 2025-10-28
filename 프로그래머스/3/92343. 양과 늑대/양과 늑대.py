from collections import deque, defaultdict

def solution(info, edges):
    
    graph = defaultdict(list)
    
    for parent, child in edges:
        graph[parent].append(child)
    
    max_sheep = 0
    q = deque([(0, 0, [0])])
    
    while q:
        sheep, wolf, possible = q.popleft()
        
        for cur in possible:
            new_sheep = sheep
            new_wolf = wolf
            
            if info[cur]==0:
                new_sheep += 1
            else:
                new_wolf += 1
            
            if new_wolf >= new_sheep:
                continue
            
            max_sheep = max(max_sheep, new_sheep)
        
            nxt_node = list(possible)
            nxt_node.remove(cur)
            nxt_node.extend(graph[cur])
            
            q.append((new_sheep, new_wolf, nxt_node))
    
    return max_sheep