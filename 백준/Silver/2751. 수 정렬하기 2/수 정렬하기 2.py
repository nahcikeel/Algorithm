import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

for j in sorted(nums):
    print(j)