n = int(input())
board = [list(input()) for _ in range(n)]

# 1. 머리 찾기
head = None
for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            head = (i, j)
            break
    if head:
        break

# 2. 심장
heart = (head[0] + 1, head[1])

# 3. 팔
l_arm = r_arm = 0
y = heart[1] - 1
while y >= 0 and board[heart[0]][y] == '*':
    l_arm += 1
    y -= 1

y = heart[1] + 1
while y < n and board[heart[0]][y] == '*':
    r_arm += 1
    y += 1

# 4. 허리
waist = 0
x = heart[0] + 1
while x < n and board[x][heart[1]] == '*':
    waist += 1
    x += 1

# 5. 다리
left_leg = right_leg = 0
leg_row = heart[0] + waist + 1

x = leg_row
y = heart[1] - 1
while x < n and board[x][y] == '*':
    left_leg += 1
    x += 1

x = leg_row
y = heart[1] + 1
while x < n and board[x][y] == '*':
    right_leg += 1
    x += 1

# 출력 (1-indexed)
print(heart[0] + 1, heart[1] + 1)
print(l_arm, r_arm, waist, left_leg, right_leg)