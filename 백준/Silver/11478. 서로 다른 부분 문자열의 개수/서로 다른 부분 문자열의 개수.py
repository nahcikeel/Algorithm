from itertools import combinations

s = input()
subs = set()

for i, j in combinations(range(len(s) + 1), 2):
    subs.add(s[i:j])

print(len(subs))