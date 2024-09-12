def GCD(a, b):
    x = min(a, b)
    y = max(a, b)
    
    if x == 0:
        return y
    else:
        return GCD(x, y%x)
    
def LCM(a, b):
    return a * b // GCD(a, b)

def solution(arr):
    arr.sort()
    lcm = arr[0]
    
    for i in arr[1:]:
        lcm = LCM(lcm, i)

    return lcm