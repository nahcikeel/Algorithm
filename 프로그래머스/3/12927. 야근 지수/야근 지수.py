import heapq

def solution(n, works):
    answer = 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for i in range(n):
        max_works = heapq.heappop(works)
        heapq.heappush(works, max_works+1)
    
    if sum(works) > 0:
        return 0
    
    for j in works:
        answer += j**2
    
    return answer