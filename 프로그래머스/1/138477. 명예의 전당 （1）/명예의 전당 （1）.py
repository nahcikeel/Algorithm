import heapq

def solution(k, score):
    answer = []
    heap = []
    
    if k>len(score):
        k = len(score)
    
    for i in range(k):
        heapq.heappush(heap, score[i])
        answer.append(heap[0])
        
    for j in range(k, len(score)):
        if score[j]>heap[0]:
            heapq.heappush(heap,score[j])
            heapq.heappop(heap)
        answer.append(heap[0])

        
    return answer