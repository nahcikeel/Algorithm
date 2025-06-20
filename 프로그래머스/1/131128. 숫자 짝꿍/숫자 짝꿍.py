from collections import Counter

def solution(X, Y):
    
    x_counter = Counter(X)
    y_counter = Counter(Y)
    nums = []
    
    for num in map(str, range(10)):
        cnt = min(x_counter[num], y_counter[num])
        nums.extend([num] * cnt)
    
    
    if not nums:
        return '-1'
    
    nums.sort(reverse=True)
    result = ''.join(nums)
    
    if result[0]=='0':
        return '0'
    
    return result