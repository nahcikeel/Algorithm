from collections import deque
import sys

n = int(sys.stdin.readline().strip())
q = deque()

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        q.append(int(command[1]))
       
    elif command[0] == 'pop':
        if len(q)>0:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if len(q)>0:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if len(q)>0:
            print(q[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if len(q)>0:
            print(q[-1])
        else:
            print(-1)