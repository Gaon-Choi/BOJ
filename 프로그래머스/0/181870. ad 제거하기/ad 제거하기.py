def solution(strArr):
    answer = []
    
    for elem in strArr:
        if elem.find('ad') < 0:
            answer.append(elem)
    
    return answer