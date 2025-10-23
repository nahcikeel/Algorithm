n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
cur_sum = 0
min_len = float('inf')

for right in range(n):
    cur_sum += nums[right]

    while cur_sum>=s:
        min_len = min(min_len, right-left+1)
        cur_sum -= nums[left]
        left += 1

print(0 if min_len == float('inf') else min_len)