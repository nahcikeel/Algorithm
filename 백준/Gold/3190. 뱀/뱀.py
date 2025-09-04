import sys
from collections import deque

n = int(input().strip())
k = int(input().strip())


apples = set()
for _ in range(k):
    r,c = map(int, input().split())
    apples.add((r,c))

L = int(input().strip())
turns = dict()
for _ in range(L):
    t,d = input().split()
    turns[int(t)] = d

snake = deque()
snake.append((1,1))
snake_set = {(1,1)}

dr = [0,1,0,-1]
dc = [1,0,-1,0]
dir_idx = 0

time = 0
while True:
    time += 1
    head_r, head_c = snake[0]
    nr = head_r + dr[dir_idx]
    nc = head_c + dc[dir_idx]

    if nr < 1 or nr > n or nc < 1 or nc > n:
        print(time)
        break
    
    if (nr, nc) in snake_set:
        print(time)
        break
    
    snake.appendleft((nr,nc))
    snake_set.add((nr,nc))

    if (nr,nc) in apples:
        apples.remove((nr,nc))
    else:
        tail = snake.pop()
        snake_set.remove(tail)

    if time in turns:
        if turns[time] == 'L':
            dir_idx = (dir_idx-1) % 4
        else:
            dir_idx = (dir_idx+1) % 4
