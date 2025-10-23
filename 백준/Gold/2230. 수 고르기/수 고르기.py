n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

left = 0
right = 0
ans = 2000000000

while left < n and right < n:
    diff = nums[right] - nums[left]

    if diff < m:
        right += 1
    else:
        if diff < ans:
            ans = diff
        left += 1

print(ans)