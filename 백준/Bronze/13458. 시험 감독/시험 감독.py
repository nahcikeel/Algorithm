from collections import deque
import math
import sys

input = sys.stdin.readline

n = int(input())
cls = deque(map(int, input().split()))
main, sub = map(int, input().split())

ans = 0
ans += n

for _ in range(n):
    now = cls.popleft()
    remain = now-main
    if remain > 0:
        ans += math.ceil(remain/sub)
    
print(ans)