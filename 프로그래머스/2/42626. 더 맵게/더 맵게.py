import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    pq = scoville
    
    while pq[0] < K and len(pq) > 1:
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        
        heapq.heappush(pq, first + 2 * second)
        answer += 1
    
    if pq[0] < K:
        return -1
    
    return answer