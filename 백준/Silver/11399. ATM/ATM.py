n = int(input())
people = list(map(int, input().split()))

result = 0
answer = 0

people.sort()

for i in range(n):
    result += people[i]
    answer += result

print(answer)