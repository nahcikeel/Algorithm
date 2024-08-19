from itertools import permutations

n,m = map(int, input().split())
numbers = list(map(int, input().split()))

answer = []
for p in permutations(numbers, m):
    answer.append(p)

answer.sort()

for a in answer:
    print(' '.join(map(str,a)))