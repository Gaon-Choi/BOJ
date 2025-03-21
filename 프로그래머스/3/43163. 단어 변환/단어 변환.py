from collections import deque

def solution(begin, target, words):
    
    def get_dist(w1, w2):
        dist = 0
        
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                dist += 1
                
        return dist
    
    answer = 0
    
    queue = deque()
    
    visited = [-1] * (len(words))
    
    queue.append([begin, 0])
    
    while len(queue) > 0:
        word, idx_ = queue.popleft()
        
        if word == target:
            return visited[idx_] + 1
        
        for idx, w in enumerate(words):
            if (visited[idx] == -1) and (get_dist(word, w) == 1):
                queue.append([w, idx])
                visited[idx] = visited[idx_] + 1
    
    return 0