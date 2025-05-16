def solution(s):
    def check_valid(s):
        stk = []
        
        for c in s:
            if c in {"(", "[", "{"}:
                stk.append(c)
            else:
                if stk and stk[-1] == "(" and c == ")":
                    stk.pop()
                elif stk and stk[-1] == "[" and c == "]":
                    stk.pop()
                elif stk and stk[-1] == "{" and c == "}":
                    stk.pop()
                else:
                    return False
                
        if stk:
            return False
        
        return True
                
    
    
    answer = 0
    
    size = len(s)
    for _ in range(size):
        s = s[1:] + s[0]
        
        if check_valid(s):
            answer += 1
    
    return answer