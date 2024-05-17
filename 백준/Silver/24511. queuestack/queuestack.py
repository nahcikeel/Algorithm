from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

q = deque()

for i in range(n):
    if a[i] == 0:
        q.append(b[i])
        
for i in c:
    q.appendleft(i)
    print(q.pop(), end=" ")