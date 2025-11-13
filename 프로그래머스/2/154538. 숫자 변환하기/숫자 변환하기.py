from collections import deque

def solution(x, y, n):
    q = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set([x])   # 이미 방문한 숫자는 재방문 방지

    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt

        # 다음 연산 후보
        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, cnt + 1))
    
    return -1 
