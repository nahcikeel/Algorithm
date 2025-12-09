def check(board):
    n = len(board)
    max_cnt = 1

    # 행 체크
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    # 열 체크
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    return max_cnt


N = int(input())
board = [list(input().strip()) for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)
