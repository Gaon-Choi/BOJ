import heapq

def solution(operations):
    answer = []
    
    idx = 0
    size = 0
    
    min_heap = []
    max_heap = []
    
    deleted = set()
    
    for query in operations:
        op, elem = query.split()
        elem = int(elem)
        
        if op == "I":
            heapq.heappush(min_heap, (elem, idx))
            heapq.heappush(max_heap, (-elem, idx))
            idx += 1
            size += 1
        else:
            if size == 0:
                continue
                
            # 최댓값 삭제
            if elem == 1:
                while max_heap:
                    del_elem, del_idx = heapq.heappop(max_heap)
                    if del_idx not in deleted:
                        deleted.add(del_idx)
                        size -= 1
                        break
            else:
                while min_heap:
                    del_elem, del_idx = heapq.heappop(min_heap)
                    if del_idx not in deleted:
                        deleted.add(del_idx)
                        size -= 1
                        break    
    
    if size == 0:
        answer.append(0)
        answer.append(0)
    else:
        while max_heap:
            val, idx = heapq.heappop(max_heap)
            
            if idx not in deleted:
                answer.append(-val)
                break
        
        while min_heap:
            val, idx = heapq.heappop(min_heap)
            
            if idx not in deleted:
                answer.append(val)
                break
    
    return answer