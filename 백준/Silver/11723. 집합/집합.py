import sys

m = int(sys.stdin.readline())
s = set()

for i in range(m):
    command = sys.stdin.readline().strip().split()

    if len(command) == 1:
        if command[0] == 'all':
            s = set([i for i in range(1,21)])
        elif command[0] == 'empty':
            s = set()
    else:
        command, x = command[0], int(command[1])
        if command == 'add':
            s.add(x)
        
        elif command == 'remove':
            s.discard(x)
        
        elif command == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        
        elif command == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)