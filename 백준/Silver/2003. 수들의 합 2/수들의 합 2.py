n,m = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
cur_sum = 0
cnt = 0

while True:
    if cur_sum == m:
        cnt += 1
    
    if (cur_sum > m) or (right == n):
        cur_sum -= nums[left]
        left += 1
    else:
        cur_sum += nums[right]
        right += 1
    
    if left == n:
        break

print(cnt)