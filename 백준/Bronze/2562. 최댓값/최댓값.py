li = []
for _ in range(9):
    li.append(int(input()))

answer = max(li)

print(answer)
print(li.index(answer)+1)