import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))

height_counts = Counter(ground)
min_time = float('inf')
result_height = 0

for target in range(257):
    removed = 0
    added = 0
    
    for height, count in height_counts.items():
        if height > target:
            removed += (height - target) * count
        elif height < target:
            added += (target - height) * count
            
    if removed + b >= added:
        time = removed * 2 + added
        
        if time <= min_time:
            min_time = time
            result_height = target

print(min_time, result_height)