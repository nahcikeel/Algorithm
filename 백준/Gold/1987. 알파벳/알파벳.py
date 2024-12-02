from collections import deque

row, col = map(int, input().split())
alp = [input().strip() for _ in range(row)]

que = deque([(0, 0, alp[0][0])])  # 시작 좌표와 경로
max_path_length = 1

dirx = [-1, 1, 0, 0]
diry = [0, 0, -1, 1]

visited = set([(0, 0, alp[0][0])])  # 방문 상태 저장

while que:
    x, y, current_path = que.popleft()
    max_path_length = max(max_path_length, len(current_path))

    for i in range(4):
        nx, ny = x + dirx[i], y + diry[i]
        if 0 <= nx < row and 0 <= ny < col:
            next_char = alp[nx][ny]
            if next_char not in current_path:
                new_path = current_path + next_char
                state = (nx, ny, new_path)
                if state not in visited:  # 중복 상태 방지
                    visited.add(state)
                    que.append((nx, ny, new_path))

print(max_path_length)
