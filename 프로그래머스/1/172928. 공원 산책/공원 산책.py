def solution(park, routes):
    h, w = len(park), len(park[0])
    
    # 시작점
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    # 방향
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    for route in routes:
        d, m = route.split()
        dx, dy = move[d]
        m = int(m)

        # 이동 가능한지 미리 확인
        nx, ny = x, y
        valid = True
        for _ in range(m):
            nx += dx
            ny += dy
            if not (0 <= nx < h and 0 <= ny < w):
                valid = False
                break
            if park[nx][ny] == 'X':
                valid = False
                break
        
        if valid:
            x, y = nx, ny

    return [x, y]
