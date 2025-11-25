N, M = map(int, input().split())

min_pack = float('inf')
min_each = float('inf')

for _ in range(M):
    a, b = map(int, input().split())
    min_pack = min(min_pack, a)
    min_each = min(min_each, b)

full_sets = N // 6
remain = N % 6

cost1 = full_sets * min_pack + remain * min_each
cost2 = (full_sets + 1) * min_pack
cost3 = N * min_each

print(min(cost1, cost2, cost3))
