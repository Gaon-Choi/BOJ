def solution(number, k):
    answer = []
    
    for c in number:
        while answer and int(answer[-1]) < int(c) and k > 0:
            answer.pop()
            k -= 1
        answer.append(c)
        
    if k == 0:
        answer = "".join(answer)
    else:
        answer = "".join(answer[:-k])
    
    return answer