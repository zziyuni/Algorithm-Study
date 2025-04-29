import heapq

def solution(book_time):
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m
    book_time = [(to_minutes(start), to_minutes(end)) for start, end in book_time]
    book_time.sort()
    end_time = []
    for start,end in book_time:
        if end_time:
            earliest = heapq.heappop(end_time)
            if earliest + 10 <=start:
                heapq.heappush(end_time,end)
            else:
                heapq.heappush(end_time,end)
                heapq.heappush(end_time,earliest)
        else:
            heapq.heappush(end_time,end)
                
    return len(end_time)