length, start = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for i in range(length):
    if fruits[i] <= start:
        start += 1
    elif fruits[i] > start:
        break

print(start)
