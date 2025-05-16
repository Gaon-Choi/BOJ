def solution(wallet, bill):
    answer = 0
    
    w_width, w_height = wallet
    b_width, b_height = bill
    
    while True:
        if b_width <= w_width and b_height <= w_height:
            break
            
        if b_width <= w_height and b_height <= w_width:
            break
            
        if b_width > b_height:
            b_width = b_width // 2
        else:
            b_height = b_height // 2
            
        answer += 1
    
    return answer