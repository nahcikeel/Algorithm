from collections import deque

l, s = map(int, input().split())

hint = {}
for _ in range(l+s):
    start,end = map(int, input().split())
    hint[start] = end

q = deque()
q.append((1,0))

visited = [False] * 101
visited[1] = True

while q:
    pos, cnt = q.popleft()

    if pos == 100:
        print(cnt)
        break

    for dice in range(1,7):
        nxt_pos = pos + dice

        if nxt_pos > 100:
            continue
        
        if nxt_pos in hint:
            nxt_pos = hint[nxt_pos]
        
        if not visited[nxt_pos]:
            visited[nxt_pos] = True
            q.append((nxt_pos, cnt+1))