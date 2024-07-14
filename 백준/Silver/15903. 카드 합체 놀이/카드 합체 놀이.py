import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(m):
    numbers.sort()

    a = numbers.pop(0)
    b = numbers.pop(0)

    numbers.append(a+b)
    numbers.append(a+b)

print(sum(numbers))