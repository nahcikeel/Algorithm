from itertools import permutations


def solution(expression):
    answer = 0
    
    # 숫자, 부호 구분
    nums = []
    ops = []
    temp = ''
    for e in expression:
        if e.isdigit():
            temp += e
        else:
            ops.append(e)
            nums.append(int(temp))
            temp = ''
    nums.append(int(temp))
    
    # 모든 조합 계산
    val = 0
    max_value = 0
    for pers in permutations(['*', '+', '-'], 3):
        nums_copy = nums[:]
        ops_copy  = ops[:]
        
        for per in pers:
            idx = 0
            while idx < len(ops_copy):
                if per == ops_copy[idx]:
                    if per == '*':
                        val = nums_copy[idx] * nums_copy[idx+1]
                    elif per == '+':
                        val = nums_copy[idx] + nums_copy[idx+1]
                    elif per == '-':
                        val = nums_copy[idx] - nums_copy[idx+1]
                        
                    nums_copy[idx] = val
                    nums_copy.pop(idx+1)
                    ops_copy.pop(idx)
                else:
                    idx += 1
                
        max_value = max(max_value, abs(nums_copy[0]))
    
    return max_value