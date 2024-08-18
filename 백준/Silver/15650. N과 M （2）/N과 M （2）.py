from itertools import combinations

n,m = map(int, input().split())
numbers = [num+1 for num in range(n)]


for p in combinations(numbers, m):
    print(' '.join(map(str,p)))