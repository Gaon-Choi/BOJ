def solution(X, Y):
    answer = ''
    
    arr1 = [0] * 10
    arr2 = [0] * 10
    
    for x in X:
        arr1[int(x)] += 1
        
    for y in Y:
        arr2[int(y)] += 1
        
    for i in reversed(range(10)):
        repeat_cnt = min(arr1[i], arr2[i])
        answer += repeat_cnt * str(i)
        
    if len(answer) == 0:
        answer = "-1"
        
    if answer[0] == "0":
        answer = "0"
    
    return answer