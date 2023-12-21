import sys

n, a = map(int, sys.stdin.readline().strip().split())
fruits = list(map(int, sys.stdin.readline().strip().split()))

fruits.sort()

for fruit in fruits:
    if fruit <= a:
        a += 1
    else:
        break

print(a)