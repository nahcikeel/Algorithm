n,r,c = map(int, input().split())

def solution(n,r,c):
    if n==0:
        return 0
        
    half = 2**(n-1)
    
    if r < half and c < half:
        return solution(n-1,r,c)
    elif r < half and c >= half:
        return solution(n-1, r, c-half) + half**2*1
    elif r >= half and c < half:
        return solution(n-1, r-half, c) + half**2*2
    else:
        return solution(n-1, r-half, c-half) + half**2*3

print(solution(n,r,c))