def solution(m, n, board):
    answer = 0
    grid = [list(row) for row in board] 
    
    total_removed = 0
    
    while True:
        remove = set()
        
        for i in range(m-1):
            for j in range(n-1):
                if grid[i][j] != '' and grid[i][j] == grid[i+1][j] == grid[i][j+1] == grid[i+1][j+1]:
                    remove.update({(i,j), (i,j+1), (i+1,j), (i+1,j+1)})
        if not remove:
            break
        
        for i,j in remove:
            grid[i][j] = ''
        total_removed += len(remove)
        
        for j in range(n):
            col = [grid[i][j] for i in range(m) if grid[i][j] != '']
            empty_count = m-len(col)
            col = ['']*empty_count + col
            for i in range(m):
                grid[i][j] = col[i]
                
    return total_removed