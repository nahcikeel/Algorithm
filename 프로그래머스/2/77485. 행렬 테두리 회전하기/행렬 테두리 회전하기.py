def solution(rows, columns, queries):
    
    graph = [[0]*columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1
    
    answer = []
    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        temp = graph[x1][y1]
        min_val = temp
        
        # 왼선
        for i in range(x1,x2):
            graph[i][y1] = graph[i+1][y1]
            min_val = min(min_val, graph[i][y1])
        
        # 아래선
        for i in range(y1,y2):
            graph[x2][i] = graph[x2][i+1]
            min_val = min(min_val, graph[x2][i])
        
        # 오른선
        for i in range(x2,x1,-1):
            graph[i][y2] = graph[i-1][y2]
            min_val = min(min_val, graph[i][y2])
        
        # 윗선
        for i in range(y2,y1,-1):
            graph[x1][i] = graph[x1][i-1]
            min_val = min(min_val, graph[x1][i])
        
        graph[x1][y1+1] = temp
        answer.append(min_val)
    
    return answer