# from itertools import product

# def solution(k, d):
    
#     arr = [i for i in range(0,d+1,k)]
#     result = list(product(arr, repeat=2))
    
#     answer = 0
#     for a,b in result:
#         if a*a + b*b <= d*d:
#             answer += 1
    
#     return answer

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        max_y = int((d**2 - x**2)**0.5)
        answer += (max_y // k) + 1
    
    
    return answer