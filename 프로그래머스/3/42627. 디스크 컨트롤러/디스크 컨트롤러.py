import heapq

def solution(jobs):
    n = len(jobs)
    
    answer = 0
    start, now, i = -1,0,0
    heap = []
    
    
    while i < n:
        for j in jobs:
            if start<j[0]<=now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap)>0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now-cur[1]
            i += 1
            
        else:
            now += 1
            
    return answer//n