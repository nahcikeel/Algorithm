from itertools import combinations_with_replacement

n,m = map(int, input().split())
numbers = [num+1 for num in range(n)]


for p in combinations_with_replacement(numbers, m):
    print(' '.join(map(str,p)))