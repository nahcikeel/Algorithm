import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
r = H / 2.0
cy = Y + r
r2 = r * r

count = 0
for _ in range(P):
    px, py = map(float, input().split())

    if X <= px <= X + W and Y <= py <= Y + H:
        count += 1
        continue

    dx = px - X
    dy = py - cy
    if dx*dx + dy*dy <= r2:
        count += 1
        continue

    dx = px - (X + W)
    dy = py - cy
    if dx*dx + dy*dy <= r2:
        count += 1

print(count)
