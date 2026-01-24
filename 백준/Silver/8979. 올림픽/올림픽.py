n, k = map(int, input().split())

countries = []
target = None

for _ in range(n):
    num, g, s, d = map(int, input().split())
    countries.append((num, g, s, d))
    if num == k:
        target = (g, s, d)

rank = 1
for num, g, s, d in countries:
    if (g, s, d) > target:
        rank += 1

print(rank)
