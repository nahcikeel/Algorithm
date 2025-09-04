n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

def merge_line(line, n):
    nums = [x for x in line if x != 0]
    result = []

    i = 0
    while i < len(nums):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            result.append(nums[i]*2)
            i += 2
        else:
            result.append(nums[i])
            i += 1
    
    while len(result) < n:
        result.append(0)
    
    return result

def move_left(board, n):
    new_board = []
    for row in board:
        new_board.append(merge_line(row, n))
    return new_board

def transpose(board, n):
    return [[board[r][c] for r in range(n)] for c in range(n)]

def reverse_rows(board):
    return [list(reversed(row)) for row in board]

def move(board, direction, n):
    if direction == 'L':
        return move_left(board, n)
    elif direction == 'R':
        b = reverse_rows(board)
        b = move_left(b, n)
        return reverse_rows(b)
    elif direction == 'U':
        b = transpose(board, n)
        b = move_left(b, n)
        return transpose(b, n)
    elif direction == 'D':
        b = transpose(board, n)
        b = reverse_rows(b)
        b = move_left(b, n)
        b = reverse_rows(b)
        return transpose(b, n)

def get_max_tile(board):
    return max(max(row) for row in board)

def dfs(board, depth, N):
    global best

    best = max(best, get_max_tile(board))

    if depth == 5:
        return
    
    for direction in ['L', 'R', 'U', 'D']:
        next_board = move(board, direction, N)
        if next_board != board:
            dfs(next_board, depth + 1, N)

best = 0
dfs(board, 0, n)
print(best)
