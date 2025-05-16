import heapq

def solution(k, score):
    answer = []
    
    pq = []
    
    for s in score:
        heapq.heappush(pq, s)
        
        if len(pq) > k:
            heapq.heappop(pq)
            
        answer.append(pq[0])          
    
    return answer