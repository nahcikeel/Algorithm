K = int(input())

dirs = []
lens = []

for _ in range(6):
    d, l = map(int, input().split())
    dirs.append(d)
    lens.append(l)

max_width = 0
max_height = 0

for i in range(6):
    d = dirs[i]
    l = lens[i]
    if d == 1 or d == 2:
        max_width = max(max_width, l)
    else:       
        max_height = max(max_height, l)

for i in range(6):
    if lens[i] == max_width:
        small_height = abs(lens[(i - 1) % 6] - lens[(i + 1) % 6])
    if lens[i] == max_height:
        small_width = abs(lens[(i - 1) % 6] - lens[(i + 1) % 6])

big = max_width * max_height
small = small_width * small_height

print((big - small) * K)
