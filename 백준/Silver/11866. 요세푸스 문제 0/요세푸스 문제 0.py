from collections import deque

ys = deque()
result = []

n,k = map(int, input().split())
for i in range(1,n+1):
    ys.append(i)

while ys:
    for _ in range(k-1):
        ys.append(ys.popleft())
    result.append(str(ys.popleft()))


print('<' + ', '.join(result) + '>')