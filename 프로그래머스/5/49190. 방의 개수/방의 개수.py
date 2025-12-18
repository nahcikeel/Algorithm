def solution(arrows):
    
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    x, y = 0, 0
    visited_nodes = set()
    visited_edges = set()

    visited_nodes.add((x, y))
    answer = 0

    for d in arrows:
        for _ in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            edge = ((x, y), (nx, ny))
            rev_edge = ((nx, ny), (x, y))

            if (edge not in visited_edges) and ((nx, ny) in visited_nodes):
                answer += 1

            visited_edges.add(edge)
            visited_edges.add(rev_edge)
            visited_nodes.add((nx, ny))

            x, y = nx, ny

    return answer
