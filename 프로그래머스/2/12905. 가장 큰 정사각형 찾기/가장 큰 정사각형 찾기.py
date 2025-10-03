def solution(board):
    answer = 0
    
    w = len(board[0])
    h = len(board)
    
    dp = [[0]*w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1], dp[i-1][j-1])+1
            answer = max(dp[i][j], answer)
            
    
    return answer**2