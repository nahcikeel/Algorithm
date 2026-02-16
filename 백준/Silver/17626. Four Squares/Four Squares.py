import math
import sys
input = sys.stdin.readline

n = int(input())

# 1개
if int(math.sqrt(n))**2 == n:
    print(1)
    exit()

# 2개
for i in range(1, int(math.sqrt(n)) + 1):
    remain = n - i*i
    if int(math.sqrt(remain))**2 == remain:
        print(2)
        exit()

# 4개 판별
temp = n
while temp % 4 == 0:
    temp //= 4

if temp % 8 == 7:
    print(4)
else:
    print(3)
