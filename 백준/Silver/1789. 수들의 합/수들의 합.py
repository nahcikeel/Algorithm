S = int(input())

total = 0
count = 0
num = 1

while total + num <= S:
    total += num
    count += 1
    num += 1

print(count)