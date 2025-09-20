import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]

mean_n = round(sum(nums)/n)

nums.sort()
center_n = nums[int(n//2)]


cnt = Counter(nums).most_common()
max_freq = cnt[0][1]
modes = [num for num, freq in cnt if freq == max_freq]

if len(modes) > 1:
    modes.sort()
    mode_n = modes[1]   # 두 번째로 작은 값
else:
    mode_n = modes[0]

ran = nums[-1] - nums[0]

print(mean_n)
print(center_n)
print(mode_n)
print(ran)