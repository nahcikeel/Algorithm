n = int(input())
nums = list(map(int, input().split()))

nums.sort()
cnt = 0

for i in range(n):
    target = nums[i]
    left = 0
    right = (n-1)

    while left<right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        
        total = nums[left] + nums[right]
        if total == target:
            cnt += 1
            break
        
        elif total > target:
            right -= 1
        else:
            left += 1
print(cnt)