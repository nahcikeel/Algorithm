n, m = map(int, input().split())

memo = {}
for _ in range(n):
    site, pw = input().split()
    memo[site] = pw

for _ in range(m):
    st = input()
    print(memo[st])