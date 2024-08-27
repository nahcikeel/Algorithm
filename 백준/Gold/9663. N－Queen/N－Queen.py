import sys

input = sys.stdin.readline

N = int(input())

answer = 0
board = [-1 for _ in range(N)]

def is_attack(board, row, col):

    for j in range(row):
        if (board[j] == col) or (abs(board[j]-col) == abs(j-row)):
            return False
    return True

def dfs(n):

    global answer

    if n == N:
        answer += 1
        return

    for i in range(N):

        if is_attack(board, n, i):
            board[n] = i
            dfs(n+1)

dfs(0)
print(answer)