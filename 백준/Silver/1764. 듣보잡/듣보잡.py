n, m = map(int,(input().split()))

listen = set()
see = set()
answer = []

for _ in range(n):
    listen.add(input())
for _ in range(m):
    see.add(input())
    
for i in listen:
    if i in see:
        answer.append(i)

answer.sort()

print(len(answer))

for j in answer:
    print(j)