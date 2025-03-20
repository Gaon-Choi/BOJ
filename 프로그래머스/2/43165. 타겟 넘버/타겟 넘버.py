from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append([0, numbers[0]])
    queue.append([0, -numbers[0]])
    
    while len(queue) > 0:
        idx, num = queue.popleft()
        
        if idx == len(numbers) - 1 and num == target:
            answer += 1
            
        if idx + 1 < len(numbers):
            queue.append([idx + 1, num + numbers[idx + 1]])
            queue.append([idx + 1, num - numbers[idx + 1]])
    
    return answer