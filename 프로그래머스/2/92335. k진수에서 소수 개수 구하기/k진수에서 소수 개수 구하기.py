import math

def is_prime(n):
    if n <= 1:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

def convert_to_k_base(n,k):
    if n == 0:
        return 0
    result = ''
    while n>0:
        remain = n%k
        result = str(remain) + result
        n = n//k
    return result
    

def solution(n, k):
    
    k_base = convert_to_k_base(n,k)
    candidates = k_base.split('0')
    
    cnt = 0
    
    for num in candidates:
        if not num:
            continue
        num = int(num)
        if is_prime(num):
            cnt += 1
    return cnt
    
    answer = -1
    return answer