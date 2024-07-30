def solution(m, n, puddles):
    
    maps = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        maps[p[1]-1][p[0]-1] = -1
    
    maps[0][0] = 1
        
    for a in range(1,n):
        if maps[a][0] == -1:
            break
        else:
            maps[a][0] = 1
        
    for b in range(1,m):
        if maps[0][b] == -1:
            break
        else:
            maps[0][b] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if maps[i][j] == -1:
                maps[i][j] = 0
            else:
                if maps[i-1][j] != -1:
                    maps[i][j] += maps[i-1][j]
                if  + maps[i][j-1] != -1:
                    maps[i][j] += maps[i][j-1]

    
    return maps[n-1][m-1] % 1000000007