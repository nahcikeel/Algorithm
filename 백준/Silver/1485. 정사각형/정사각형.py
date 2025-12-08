def dist2(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def is_square(pts):
    d = []
    for i in range(4):
        for j in range(i+1, 4):
            d.append(dist2(pts[i], pts[j]))

    d.sort()

    if d[0] == 0:
        return 0

    if d[0] == d[1] == d[2] == d[3] and d[4] == d[5]:
        return 1
    return 0


T = int(input())
for _ in range(T):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    print(is_square(points))
