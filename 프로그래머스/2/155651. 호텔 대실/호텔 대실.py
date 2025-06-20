import heapq

def to_min(time):
    h,m = map(int, time.split(':'))
    return h*60+m


def solution(book_time):
    answer = 1
    
    books = []
    for start,end in book_time:
        books.append([to_min(start), to_min(end)+10])    
    books.sort()
    
    rooms = []
    for start, end in books:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    
    return len(rooms)