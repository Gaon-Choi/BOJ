def solution(data, col, row_begin, row_end):
    # 데이터 정렬
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    # S_i 계산
    s = []
    
    for i in range(len(data)):
        temp = 0
        
        for elem in data[i]:
            temp += elem % (i + 1)
            
        s.append(temp)
        
    answer = s[row_begin - 1]
    
    for i in range(row_begin, row_end):
        answer = answer ^ s[i]
        
    return answer