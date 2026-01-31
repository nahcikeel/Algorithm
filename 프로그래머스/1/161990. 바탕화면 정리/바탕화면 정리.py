def solution(wallpaper):
    answer = []
    
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    min_n, min_m = n, m
    max_n, max_m = 0, 0
    
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == '#':
                min_n = min(min_n, i)
                min_m = min(min_m, j)
                max_n = max(max_n, i)
                max_m = max(max_m, j)    
    
    return [min_n, min_m, max_n + 1, max_m + 1]