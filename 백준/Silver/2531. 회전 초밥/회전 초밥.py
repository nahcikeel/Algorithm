n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

sushi += sushi[:k-1]

max_count = 0

for i in range(n):
    window = sushi[i:i+k]
    kinds = set(window)
    cnt = len(kinds)
    if c not in kinds:
        cnt += 1
    max_count = max(max_count, cnt)
    
print(max_count)