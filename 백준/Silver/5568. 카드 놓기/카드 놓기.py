from itertools import permutations

N = int(input())
K = int(input())
cards = [input().strip() for _ in range(N)]

result = set()

for p in permutations(cards, K):
    num = ''.join(p)
    result.add(num)

print(len(result))
