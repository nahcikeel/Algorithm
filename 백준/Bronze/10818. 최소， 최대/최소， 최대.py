n = input()
numbers = list(map(int, input().split()))
numbers.sort()
print(min(numbers), max(numbers))