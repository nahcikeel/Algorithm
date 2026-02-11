
def to_base(num,n):
    digits = '0123456789ABCDEF'
    
    if num==0:
        return '0'
    
    res = []
    while num:
        num,r = divmod(num,n)
        res.append(digits[r])
    return ''.join(reversed(res))

def solution(n, t, m, p):
    answer = []
    
    num = 0
    while len(answer) < t*m:
        res = to_base(num,n)
        answer.extend(res)
        num += 1
    
    answer = ''.join(answer[p-1:m*t:m])
    return answer