import sys
from collections import Counter

input = sys.stdin.readline

r,c,k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(3)]
def operate(nums, is_row=True):
    new_arr = []
    max_len = 0

    # 행 계산
    if is_row:
        for row in nums:
            counter = Counter(x for x in row if x != 0)
            sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))
            new_row = []
            for num,cnt in sorted_items:
                new_row.extend([num,cnt])
            new_arr.append(new_row[:100])
            max_len = max(max_len, len(new_row))

        for row in new_arr:
            row.extend([0]*(max_len-len(row)))
        return new_arr
    
    # 열 계산
    else:
        tran = list(map(list, zip(*nums)))
        new_tran = operate(tran, True)
        return [list(x) for x in zip(*new_tran)]


time = 0
while time<=100:
    if (r-1)<len(nums) and (c-1)<len(nums[0]) and nums[r-1][c-1] == k:
        print(time)
        break
    
    if len(nums) >= len(nums[0]):
        nums = operate(nums, True)
    else:
        nums = operate(nums, False)
    
    time += 1

else:
    print(-1)


