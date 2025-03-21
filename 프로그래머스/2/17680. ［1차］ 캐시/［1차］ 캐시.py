from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    queue = deque([0] * cacheSize)
    
    for i in range(len(cities)):
        city_name = cities[i].lower()
        
        if city_name in queue:
            queue.remove(city_name)
            queue.append(city_name)
            answer += 1
        else:
            if queue:
                queue.popleft()
                queue.append(city_name)
            answer += 5
    
    return answer