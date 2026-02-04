import heapq


def solution(n, k, enemy):
    
    heap = []
    for i,e in enumerate(enemy):
        heapq.heappush(heap, -e)
        
        n -= e
        if n<0:
            if k==0:
                return i
            k -= 1
            n += -heapq.heappop(heap)

    return len(enemy)