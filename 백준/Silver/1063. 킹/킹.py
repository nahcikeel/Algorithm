def to_coord(pos):
    return ord(pos[0]) - ord('A'), int(pos[1]) - 1

def to_pos(x, y):
    return chr(x + ord('A')) + str(y + 1)

king_pos, rock_pos, N = input().split()
N = int(N)
king_x, king_y = to_coord(king_pos)
rock_x, rock_y = to_coord(rock_pos)

directions = {
    'R': (1,0), 'L':(-1,0), 'B':(0,-1), 'T':(0,1),
    'RT':(1,1), 'LT':(-1,1), 'RB':(1,-1), 'LB':(-1,-1)
}

for _ in range(N):
    move = input().strip()
    dx, dy = directions[move]
    
    nx, ny = king_x + dx, king_y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        if (nx, ny) == (rock_x, rock_y):
            rx, ry = rock_x + dx, rock_y + dy
            if 0 <= rx < 8 and 0 <= ry < 8:
                king_x, king_y = nx, ny
                rock_x, rock_y = rx, ry
        else:
            king_x, king_y = nx, ny

print(to_pos(king_x, king_y))
print(to_pos(rock_x, rock_y))
