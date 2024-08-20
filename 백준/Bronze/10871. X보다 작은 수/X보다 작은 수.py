n,m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
for num in numbers:
    if num < m:
        answer.append(num)

print(*answer)