def solution(s):
    answer = ""
    
    number = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    
    temp = ""
    
    for c in s:
        # 알파벳인 경우
        if c.isalpha():
            temp += c
        else:
            answer += c
            
        if temp in number:
            answer += str(number[temp])
            temp = ""
            
    if len(temp) > 0:
        answer += str(number[temp])
        
    answer = int(answer)
    
    return answer