import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        
        start_in = (x1 - cx)**2 + (y1 - cy)**2 < r * r
        end_in = (x2 - cx)**2 + (y2 - cy)**2 < r * r
        
        if start_in != end_in:
            count += 1
    
    print(count)
