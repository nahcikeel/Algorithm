import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)